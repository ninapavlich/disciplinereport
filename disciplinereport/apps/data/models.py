from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property


from carbon.atoms.models.user import StreetAddressAtom, PersonAtom, \
    PhoneContactAtom, StreetAddressMolecule
from carbon.compounds.page.models import Page as BasePage
from carbon.atoms.models.content import TagMolecule as BaseTagMolecule
"""
Country
Country Region
State
State Region
School District
School
Teacher(s)
Classroom
"""

"""
Annual Report:
- Key Findings Tables
- District Data
- Solutions for Action
- School Data
- Spotlight on Charters
"""

class BasePerson(PersonAtom, PhoneContactAtom, StreetAddressMolecule):
    job_title = models.CharField(_("Job Title"), max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), null=True, blank=True)

    class Meta:
        abstract = True


class SchoolBoardRepresentative(BasePerson):
    school_district = models.ForeignKey('SchoolDistrict')

class SchoolRepresentative(BasePerson):
    school = models.ForeignKey('School')

class BaseEntity(BasePage, StreetAddressAtom):

    email = models.CharField(_('Email'), max_length=255, blank=True, null=True) 
    phone_number = models.CharField(_('Phone Number'), max_length=255, blank=True, null=True) 
    website = models.CharField(_('Website'), max_length=255, blank=True, null=True) 
    
    def get_google_map_link_url(self):
        return u'https://www.google.com/maps/place/%s,+%s,+%s+%s/%s,%s'%(self.street_1, self.city, self.state, self.zipcode, self.latitude, self.longitude)

    def get_google_map_image_url(self):

        return u'https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zo\
om=10&scale=false&size=400x250&maptype=roadmap&format=png&visual_refresh=\
true&markers=color:0x85200c|label:|%s,%s'%(self.latitude, self.longitude, self.latitude, self.longitude)

    class Meta:
        abstract = True


class SchoolYear(BaseTagMolecule):
    pass

class CityRegion(BaseTagMolecule):
    pass


class State(BaseEntity):
    pass

class StateRegion(BaseEntity):
    pass

class County(BaseEntity):
    pass

class SchoolType(BaseEntity):
    pass

class SchoolDistrict(BaseEntity):

    state_obj = models.ForeignKey('State')
    state_region = models.ForeignKey('StateRegion')
    county = models.ForeignKey('County')
    district_code = models.CharField(_("District Code"), max_length=255, blank=True, null=True)

    
    def get_data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self)

    @cached_property
    def latest_data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self).first()

    @cached_property
    def data_columns(self):
        return self.latest_data.__class__.data_columns_formatted()

    @cached_property
    def normalized_data_columns(self):
        return self.latest_data.__class__.normalized_data_columns_formatted()


    def get_absolute_url(self):
       return reverse('district_detail',  args=[self.slug] )

    @cached_property
    def hierarchical_children(self):
        return []


class School(BaseEntity):
    """
    district :FK
    school board: FK
    previous known names
    contact info
    school message
    address
    contact links
    """
    
    school_district = models.ForeignKey('SchoolDistrict')
    city_region = models.ForeignKey('CityRegion')
    school_type = models.ForeignKey('SchoolType')

    is_charter = models.BooleanField(default=False)
    is_pathways = models.BooleanField(default=False)


class BaseDatum(BasePage):
    """
    School Year
    oss
    iss
    rtli
    1st offense
    disparity
    contribution
    turnover
    attendance
    math
    reading
    writing
    spf
    """

    help = {
        'population':"",
        'soc':"Percentage students of color.",
        'frl':"Percentage students with free and reduced lunch.",
        'ell':"Percentage english language learners.",
        'sped':"Percentage students receiving Special Education services.",
        'iss': "In School Suspension rates per 100 students.",
        'oss': "Out of School Suspension rates per 100 students.",
        'expulsions':"",
        'rtl': "Referrals to law enforcement rates per 100 students.",
        'one_offense': "Percentage of students with at least one offense.",
        'school_arrests':"",
        'racial_disparity_impact': "",
        'district_inequality_contribution':"",
        'student_turnover': "",
        'poor_attendance': "",
        'proficient_math': "Percentage students proficient or better in Math",
        'proficient_reading': "Percentage students proficient or better in Reading",
        'proficient_writing': "Percentage students proficient or better in Writing"
    }



    #FACTS
    school_year = models.ForeignKey('SchoolYear')
    
    population = models.IntegerField(_('Student Population'), blank=True, null=True,
        help_text=help['population'],)
    soc = models.FloatField(_('Students of Color'), blank=True, null=True,
        help_text=help['soc'],)
    frl = models.FloatField(_('Free and Reduced Lunch'), blank=True, null=True,
        help_text=help['frl'],)
    ell = models.FloatField(_('English Language Learners'), blank=True, null=True,
        help_text=help['ell'],)
    sped = models.FloatField(_('Exceptional Learners'), blank=True, null=True,
        help_text=help['sped'],)

    #SCHOOL-TO-JAIL TRACK
    iss = models.FloatField(_('In-school Suspensions'), blank=True, null=True,
        help_text=help['iss'],)
    oss = models.FloatField(_('Out-of-school Suspensions'), blank=True, null=True,
        help_text=help['oss'],)
    expulsions = models.FloatField(_('Expulsions'), blank=True, null=True,
        help_text=help['expulsions'],)
    rtl = models.FloatField(_('Referrals to Law Enforcement'), blank=True, null=True,
        help_text=help['rtl'],)
    one_offense = models.FloatField(_('One Offense'), blank=True, null=True,
        help_text=help['one_offense'],)
    school_arrests = models.FloatField(_('School Arrests'), blank=True, null=True,
        help_text=help['school_arrests'],)
    racial_disparity_impact = models.FloatField(_('Racial Disparity Impact'), 
        blank=True, null=True, help_text=help['racial_disparity_impact'],)
    district_inequality_contribution = models.FloatField(_('District Inequality Contribution'), 
        blank=True, null=True, help_text=help['district_inequality_contribution'],)

    #STUDENT PUSHOUT
    student_turnover = models.FloatField(_('Student Turnover'), 
        blank=True, null=True, help_text=help['student_turnover'],)

    poor_attendance = models.FloatField(_('Poor Attendance'), 
        blank=True, null=True, help_text=help['poor_attendance'],)

    

    #ACADEMIC ACHIEVEMENT
    proficient_math = models.FloatField(_('Proficient Math'), 
        blank=True, null=True, help_text=help['proficient_math'],)
    proficient_reading = models.FloatField(_('Proficient Reading'), 
        blank=True, null=True, help_text=help['proficient_reading'],)
    proficient_writing = models.FloatField(_('Proficient Writing'), 
        blank=True, null=True, help_text=help['proficient_writing'],)

    @cached_property
    def get_data_column_values(self):
        columns = self.__class__.data_columns_formatted()
        for column in columns:
            column['value'] = getattr(self, column['slug'])        
        return columns


    @cached_property
    def get_normalized_data_column_values(self):
        columns = self.__class__.normalized_data_columns_formatted()
        for column in columns:
            column['value'] = getattr(self, column['slug'])        
        return columns


    @classmethod
    def columns(cls):
        return ['school_year', 'population', 'soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'racial_disparity_impact', 
        'district_inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def data_columns(cls):
        return ['population', 'soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'racial_disparity_impact', 
        'district_inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def normalized_data_columns(cls):
        return ['soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def data_columns_formatted(cls):
        raw_columns = cls.data_columns()
        output = []
        for column in raw_columns:
            field = cls._meta.get_field(column)
            output.append({
                'title':field.verbose_name.title(),
                'slug':column
            })            
        return output


    @classmethod
    def normalized_data_columns_formatted(cls):
        raw_columns = cls.normalized_data_columns()
        output = []
        for column in raw_columns:
            field = cls._meta.get_field(column)
            output.append({
                'title':field.verbose_name.title(),
                'slug':column
            })            
        return output
    
    class Meta:
        abstract = True


class SchoolDatum(BaseDatum):
    school = models.ForeignKey('School')

    help = {
        
        'district_inequality_contribution': "",
        'spf_growth_points': ""
    }
    

    #ACADEMIC ACHIEVEMENT
    spf_growth_points = models.FloatField(_('SPF Groth Points'), 
        blank=True, null=True, help_text=help['spf_growth_points'],)

    @classmethod
    def columns(cls):
        return ['school_year', 'population', 'soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'ratial_disparity_impact', 
        'district_inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing', 'spf_growth_points']

class SchoolDistrictDatum(BaseDatum):
    school_district = models.ForeignKey('SchoolDistrict')

class StateDatum(BaseDatum):
    state = models.ForeignKey('State')    








