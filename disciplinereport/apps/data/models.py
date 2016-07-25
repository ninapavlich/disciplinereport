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
        color = '941825'
        return 'https://api.mapbox.com/v4/mapbox.streets/pin-m-marker+%s(%s,%s)/%s,%s,10/400x250@2x.png?access_token=%s'%(color, self.longitude, self.latitude, self.longitude, self.latitude, settings.MAPBOX_ACCESS_TOKEN)
#         return u'https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zo\
# om=10&scale=false&size=400x250&maptype=roadmap&format=png&visual_refresh=\
# true&markers=color:0x85200c|label:|%s,%s'%(self.latitude, self.longitude, self.latitude, self.longitude)

    class Meta:
        abstract = True

class Tooltip(BaseTagMolecule):
    @cached_property
    def tag_children(self):
        return []

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

    

    def get_value_difference(self, attribute_name):
        current_data = self.latest_data
        previous_data = self.previous_data
        attribute_name_formatted = BaseDatum.format_column(attribute_name)
        

        if current_data and not previous_data:
            message = "%s was %s in %s"%(attribute_name_formatted, getattr(current_data, attribute_name), current_data.school_year)

            return {
                'difference':0,
                'current_data':current_data,
                'previous_data':None,
                'attribute_name':attribute_name,
                'attribute_name_formatted':attribute_name_formatted,
                'verbose':message
            }

        if previous_data and not current_data:
            message = "%s was %s in %s"%(attribute_name_formatted, getattr(previous_data, attribute_name), previous_data.school_year)

            return {
                'difference':0,
                'current_data':None,
                'previous_data':previous_data,
                'attribute_name':attribute_name,
                'attribute_name_formatted':attribute_name_formatted,
                'verbose':message
            }

        difference = getattr(current_data, attribute_name) - getattr(previous_data, attribute_name)

        if difference == 0:
            message = "%s stayed the same from %s to %s at %s"%(attribute_name_formatted, previous_data.school_year, current_data.school_year, getattr(current_data, attribute_name))
        elif difference > 0:
            message = "%s increased to %s in %s from %s in %s"%(attribute_name_formatted, getattr(current_data, attribute_name), current_data.school_year, getattr(previous_data, attribute_name), previous_data.school_year)
        else:
            message = "%s decreased to %s in %s from %s in %s"%(attribute_name_formatted, getattr(current_data, attribute_name), current_data.school_year, getattr(previous_data, attribute_name), previous_data.school_year)
        return {
            'difference':difference,
            'current_data':current_data,
            'previous_data':previous_data,
            'attribute_name':attribute_name,
            'attribute_name_formatted':attribute_name_formatted,
            'verbose':message
        }

        

    @cached_property
    def data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self).select_related('school_year').select_related('school_district')

    @cached_property
    def latest_data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self).select_related('school_year').select_related('school_district').first()

    @cached_property
    def previous_data(self):
        try:
            return SchoolDistrictDatum.objects.filter(school_district=self).select_related('school_year').select_related('school_district')[1]
        except:
            return None

    @cached_property
    def columns(self):
        return self.latest_data.__class__.columns_formatted()

    @cached_property
    def data_columns(self):
        return self.latest_data.__class__.data_columns_formatted()

    @cached_property
    def normalized_data_columns(self):
        return self.latest_data.__class__.normalized_data_columns_formatted()


    def get_absolute_url(self):
       return reverse('district_detail',  args=[self.slug] )

    def get_data_url(self):
       return reverse('district_detail_download',  args=[self.slug] )

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
        'expulsions':"Expulsions per 100 students.",
        'rtl': "Referrals to law enforcement rates per 100 students.",
        'one_offense': "Percentage of students with at least one offense.",
        'school_arrests':"School related arrests per 100 students.",
        'racial_disparity_impact': "",
        'inequality_contribution':"",
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
    inequality_contribution = models.FloatField(_('District Inequality Contribution'), 
        blank=True, null=True, help_text=help['inequality_contribution'],)

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

    @property
    def entity(self):
        return None

    @cached_property
    def column_values(self):
        columns = self.__class__.columns_formatted()
        for column in columns:
            column['value'] = getattr(self, column['slug'])        
        return columns


    @cached_property
    def data_column_values(self):
        columns = self.__class__.data_columns_formatted()
        for column in columns:
            column['value'] = getattr(self, column['slug'])        
        return columns


    @cached_property
    def normalized_data_column_values(self):
        columns = self.__class__.normalized_data_columns_formatted()
        for column in columns:
            column['value'] = getattr(self, column['slug'])        
        return columns


    @classmethod
    def columns(cls):
        return ['entity', 'school_year', 'population', 'soc', 'frl', 'ell', 'sped',
        'iss', 'oss', 'rtl', 
        'one_offense', 'racial_disparity_impact', 
        'inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def data_columns(cls):
        return ['population', 'soc', 'frl', 'ell', 'sped',
        'iss', 'oss', 'rtl', 
        'one_offense', 'racial_disparity_impact', 
        'inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def normalized_data_columns(cls):
        return ['soc', 'frl', 'ell', 'sped',
         'iss', 'oss', 'rtl', 
        'one_offense', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']

    @classmethod
    def columns_formatted(cls):
        return cls.format_columns(cls.columns())

    @classmethod
    def data_columns_formatted(cls):
        return cls.format_columns(cls.data_columns())

    @classmethod
    def normalized_data_columns_formatted(cls):
        return cls.format_columns(cls.normalized_data_columns())

    @classmethod
    def format_columns(cls, raw_columns):
        output = []
        for column in raw_columns:
            output.append({
                'title':cls.format_column(column),
                'slug':column
            })            
        return output

    @classmethod
    def format_column(cls, column):
        try:
            field = cls._meta.get_field(column)
            field_name = field.verbose_name.title()
        except:
            field_name = column
        return field_name

    class Meta:
        abstract = True


class SchoolDatum(BaseDatum):
    school = models.ForeignKey('School')

    help = {
        
        'inequality_contribution': "",
        'spf_growth_points': ""
    }
    
    @property
    def entity(self):
        return self.school

    #ACADEMIC ACHIEVEMENT
    spf_growth_points = models.FloatField(_('SPF Groth Points'), 
        blank=True, null=True, help_text=help['spf_growth_points'],)

    @classmethod
    def columns(cls):
        return ['school_year', 'population', 'soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'ratial_disparity_impact', 
        'inequality_contribution', 'student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing', 'spf_growth_points']

class SchoolDistrictDatum(BaseDatum):
    school_district = models.ForeignKey('SchoolDistrict')

    @property
    def entity(self):
        return self.school_district

class StateDatum(BaseDatum):
    state = models.ForeignKey('State')    

    @property
    def entity(self):
        return self.state








