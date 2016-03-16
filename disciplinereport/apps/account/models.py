from django.db import models
from django.conf import settings

from carbon.atoms.models.user import StreetAddressAtom
from carbon.compounds.account.models import User as BaseUser
from carbon.compounds.account.models import Address as BaseAddress
from carbon.compounds.account.models import UserGroup as BaseUserGroup
from carbon.compounds.account.models import UserGroupMember as BaseUserGroupMember
from carbon.compounds.account.models import Organization as BaseOrganization
from carbon.compounds.account.models import OrganizationMember as BaseOrganizationMember
from carbon.compounds.account.models import SocialContactLink as BaseSocialContactLink

from django.utils.functional import cached_property


class User(BaseUser):

    directory_contact_description = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)


    @cached_property
    def social_links(self):
        return SocialContactLink.objects.filter(user=self).order_by('order')

class Address(BaseAddress):

    pass

class UserGroupMember(BaseUserGroupMember):

    group = models.ForeignKey('account.UserGroup', 
        blank=True, null=True)    

class UserGroup(BaseUserGroup):
    member_class = UserGroupMember
    pass    


class Organization(BaseOrganization, StreetAddressAtom):

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
        


    @cached_property
    def social_links(self):
        return OrganizationSocialContactLink.objects.filter(organization=self).order_by('order')

class OrganizationMember(BaseOrganizationMember):

    organization = models.ForeignKey('Organization', blank=True, null=True)

class SocialContactLink(BaseSocialContactLink):
    pass


class OrganizationSocialContactLink(BaseSocialContactLink):

    organization = models.ForeignKey('Organization')    