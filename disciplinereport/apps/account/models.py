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

    project_role = models.CharField(max_length=255, blank=True, null=True)


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
        color = '941825'
        return 'https://api.mapbox.com/v4/mapbox.streets/pin-m-marker+%s(%s,%s)/%s,%s,10/400x250@2x.png?access_token=%s'%(color, self.longitude, self.latitude, self.longitude, self.latitude, settings.MAPBOX_ACCESS_TOKEN)
    
        


    @cached_property
    def social_links(self):
        return OrganizationSocialContactLink.objects.filter(organization=self).order_by('order')

class OrganizationMember(BaseOrganizationMember):

    organization = models.ForeignKey('Organization', blank=True, null=True)

class SocialContactLink(BaseSocialContactLink):
    pass


class OrganizationSocialContactLink(BaseSocialContactLink):

    organization = models.ForeignKey('Organization')    

    class Meta:
        ordering = ['order']