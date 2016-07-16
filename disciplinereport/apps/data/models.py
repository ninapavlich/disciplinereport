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
om=7&scale=2&size=400x200&maptype=roadmap&format=png&visual_refresh=\
true&markers=color:0x0077bd|label:|%s,%s&style=feature:water|element:\
geometry|color:0xe9e9e9|lightness:17|&style=feature:landscape|element\
:geometry|color:0xf5f5f5|lightness:20|&style=feature:road.highway|ele\
ment:geometry.fill|color:0xffffff|lightness:17|&style=feature:road.hi\
ghway|element:geometry.stroke|color:0xffffff|lightness:29|weight:0.2|\
&style=feature:road.arterial|element:geometry|color:0xffffff|lightnes\
s:18|&style=feature:road.local|element:geometry|color:0xffffff|lightn\
ess:16|&style=feature:poi|element:geometry|color:0xf5f5f5|lightness:2\
1|&style=feature:poi.park|element:geometry|color:0xdedede|lightness:2\
1|&style=element:labels.text.stroke|visibility:on|color:0xffffff|ligh\
tness:16|&style=element:labels.text.fill|saturation:36|color:0x333333\
|lightness:40|&style=element:labels.icon|visibility:off|&style=featur\
e:transit|element:geometry|color:0xf2f2f2|lightness:19|&style=feature\
:administrative|element:geometry.fill|color:0xfefefe|lightness:20|&st\
yle=feature:administrative|element:geometry.stroke|color:0xfefefe|lig\
        htness:17|weight:1.2|'%(self.latitude, self.longitude, self.latitude, self.longitude)

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

class SchoolDistrict(BaseEntity):

    state_region = models.ForeignKey('StateRegion')
    
    def get_data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self)

    @cached_property
    def latest_data(self):
        return SchoolDistrictDatum.objects.filter(school_district=self).first()

    def get_absolute_url(self):
       return reverse('district_detail',  args=[self.slug] )


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


    @classmethod
    def columns(cls):
        return ['school_year', 'population', 'soc', 'frl', 'iss', 'oss', 'rtl', 
        'one_offense', 'ratial_disparity_impact','student_turnover',
        'poor_attendance', 'proficient_math', 'proficient_reading',
        'proficient_writing']
    
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








