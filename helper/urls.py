from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('redirect-after-login/', views.redirect_after_login, name='redirect_after_login'),
    path('subscription/', views.subscription_selection, name='subscription_selection'),
    path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
    path('dashboard/guide/', views.dashboard_student, name='dashboard_guide'),
    path('delete-document/<int:doc_id>/', views.delete_document, name='delete_document'),
    path('edit-document/<int:doc_id>/', views.edit_document, name='edit_document'),
    path('universities/', views.universities_list, name='universities_list'),
    path('university/<int:uni_id>/faculties/', views.university_faculties, name='university_faculties'),
    path('pay-fee/<int:uni_id>/', views.pay_application_fee, name='pay_application_fee'),
    path('pay-fee/<int:uni_id>/instructions/', views.pay_application_fee_instructions, name='pay_application_fee_instructions'),
    path('pay-all-fees/', views.pay_all_application_fees, name='pay_all_application_fees'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),
]