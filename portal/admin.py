from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from import_export.formats import base_formats
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Applicant, Waitlist, OccupiedList


# class QueuerResource(resources.ModelResource):
#     class Meta:
#         model = Queuer


# class DependantResource(resources.ModelResource):
#     class Meta:
#         model = Dependant

# class CustomDependantAdmin(admin.ModelAdmin):
#     """Admin View for Dependant"""

#     resource_class = DependantResource
#     readonly_fields = ("__all__")
#     list_display = (
#         "queuer",
#         "name",
#         "contact_number",
#         "photo"
#     )

class ApplicantResource(resources.ModelResource):
    class Meta:
        model = Applicant

# class DocumentResource(resources.ModelResource):
#     class Meta:
#         model = Documents

# class DocumentsAdmin(admin.ModelAdmin):
#     resource_class = DocumentResource
#     readonly_fields = ('applicant', )

class HCUAdminSite(admin.AdminSite):
    site_header = "HCU Admin"
    site_title = "HCU Admin Portal"
    index_title = "Welcome to the HCU admin portal"

class HCUAdminApplicantResource(resources.ModelResource):
    class Meta:
        model = Applicant

class HCUAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = HCUAdminApplicantResource
    list_display = (
        'name',
        'roll_number',
        'email',
        'department',
        "waitlist_Type1",
        "waitlist_Tulsi",
        "waitlist_MRSB",
        # "all_verified",
        "occupied_Type1",
        "occupied_Tulsi",
        "occupied_MRSB"
    )

    search_fields = ("name", "roll_number")
    list_filter = (
        "occupied_Type1",
        "occupied_Tulsi",
        "occupied_MRSB",
    )
    readonly_fields = ('name', 'roll_number', 'date_of_registration', 'department',
                       'email', 'phone_number', 'permanent_address', 'scholarship', 'date_of_scholarship', 'course_work_completed_on',
                       'course_work_completed_by', 'scholarship_awarded_upto', 'acad_details_verified', 'acad_details_verification_date', 'marriage_certificate', 'joint_photograph_with_spouse',
                       'coursework_grade_sheet', 'recommendation_of_guide_for_accomodation', 'spouse_name', 'spouse_roll_number', 'spouse_designation', 'application_received_by_hcu_date')
    exclude = ['acad_details_verification_date']
    fields = ('name', 'roll_number', 'date_of_registration', 'department', 'email', 'phone_number', 'permanent_address', 'scholarship',
              'date_of_scholarship', 'course_work_completed_on', 'course_work_completed_by', 'marriage_certificate', 'joint_photograph_with_spouse',
              'coursework_grade_sheet', 'recommendation_of_guide_for_accomodation', 'spouse_name', 'spouse_roll_number', 'spouse_designation',
              'marriage_certificate_verified', 'joint_photograph_with_spouse_verified', 'coursework_grade_sheet_verified', 'recommendation_of_guide_for_accomodation_verified',
              'feedback', 'application_received_by_hcu_date', 'verified_time')

    def get_queryset(self, request):
        qs = super(HCUAdmin, self).get_queryset(request)
        
        return qs.filter(acad_details_verified=True).order_by('date_applied')

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.HTML,
        )

        return [f for f in formats if f().can_export()]

class AcadAdminSite(admin.AdminSite):
    site_header = "Academic Section"
    site_title = "Academic Section Admin Portal"
    index_title = "Welcome to the Academic Section Admin Portal"

class AcadAdminApplicantResource(resources.ModelResource):
    class Meta:
        model = Applicant
        # fields = ('name', 'roll_number', 'date_of_registration', 'department',
        # 'email', 'phone_number', 'permanent_address', 'scholarship', 'course_work_completed_on',
        # 'course_work_completed_by')
class AcadAdmin(admin.ModelAdmin):
    resource_class = AcadAdminApplicantResource
    list_display = (
        'name',
        'roll_number',
        'department',
        'acad_details_verified'
    )
    fields = ('name', 'roll_number', 'date_of_registration', 'department',
              'email', 'phone_number', 'permanent_address', 'scholarship', 'date_of_scholarship', 'course_work_completed_on',
              'course_work_completed_by', 'scholarship_awarded_upto', 'acad_details_verified', 'acad_details_verification_date')
    readonly_fields = ('name', 'roll_number', 'date_of_registration', 'department',
                       'email', 'phone_number', 'permanent_address', 'scholarship', 'date_of_scholarship', 'course_work_completed_on',
                       'course_work_completed_by')



class ApplicantAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ApplicantResource
    list_display = (
        'name',
        'roll_number',
        'email',
        'department',
        "waitlist_Type1",
        "waitlist_Tulsi",
        "waitlist_MRSB",
        # "all_verified",
        "occupied_Type1",
        "occupied_Tulsi",
        "occupied_MRSB"
    )

    search_fields = ("name", "roll_number")
    list_filter = (
        "occupied_Type1",
        "occupied_Tulsi",
        "occupied_MRSB",
    )

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.CSV,
            base_formats.HTML,
        )

        return [f for f in formats if f().can_export()]

# class CustomQueuerAdmin(ExportMixin, admin.ModelAdmin):
#     """Admin View for Queuer"""

#     resource_class = QueuerResource
#     readonly_fields = ("date_applied",)
#     list_display = (
#         "name",
#         # "building_applied",
#         "waitlist_Type1",
#         "waitlist_Tulsi",
#         "waitlist_MRSB",
#         "all_verified",
#         "placed",
#         "contact_number",
#         "email",
#         # "marriage_certificate",
#     )
#     list_filter = (
#         "building",
#         # "tulsi",
#         # "mrsb",
#         # "type1",
#         "placed",
#     )
#     search_fields = ("name", "contact_number")
#     # fieldsets = (
#     #     (None, {'fields': ["building_applied", "placed", "room_number", ]}),

#     #     ("Personal Info", {
#     #         'fields': ["name",
#     #                    "contact_number",
#     #                    "email", ]
#     #     }),

#     #     ("Certificates", {
#     #         'fields': ["marriage_certificate"]
#     #     })
#     # )
#     form = QueuerAdminForm

#     def get_export_formats(self):
#         formats = (
#             base_formats.XLS,
#             base_formats.XLSX,
#             base_formats.CSV,
#             base_formats.HTML,
#         )

#         return [f for f in formats if f().can_export()]

#     def Mark_as_placed(self, modeladmin, news, queryset):
#         queryset.update(placed=True)

#     def Mark_as_not_placed(self, modeladmin, news, queryset):
#         queryset.update(placed=False)

#     actions = [
#         Mark_as_placed,
#         Mark_as_not_placed,
#     ]

from .forms import MailingListForm
class WaitlistAdmin(admin.ModelAdmin):
    form = MailingListForm
    list_display = ('building', 'view_applicants_link',)
    filter_horizontal = ("applicant", )
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "applicant":
            kwargs['queryset'] = Applicant.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def view_applicants_link(self, obj):
        count = obj.applicant.count()
        url = (
            reverse("admin:portal_applicant_changelist")
            + "?"
            + urlencode({"waitlist__id": f"{obj.id}"})
        )

        return format_html('<a href="{}">{} Applicants</a>', url, count)

    view_applicants_link.short_description = "Applicants"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        return response
    
class OccupiedListAdmin(admin.ModelAdmin):
    list_display = ('building', 'view_applicants_link',)
    filter_horizontal = ("applicant", )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "applicant":
            kwargs['queryset'] = Applicant.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def view_applicants_link(self, obj):
        count = obj.applicant.count()
        url = (
            reverse("admin:portal_applicant_changelist")
            + "?"
            + urlencode({"occupiedlist__id": f"{obj.id}"})
        )

        return format_html('<a href="{}">{} Applicants</a>', url, count)

    view_applicants_link.short_description = "Applicants"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        return response

hcu_admin_site = HCUAdminSite(name='hcu_admin')
acad_admin_site = AcadAdminSite(name='acad_admin')
acad_admin_site.register(Applicant, AcadAdmin)
hcu_admin_site.register(Applicant, HCUAdmin)
hcu_admin_site.register(Waitlist, WaitlistAdmin)
hcu_admin_site.register(OccupiedList, OccupiedListAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Waitlist, WaitlistAdmin)
admin.site.register(OccupiedList, OccupiedListAdmin)