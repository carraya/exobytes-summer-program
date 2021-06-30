from django.urls import path
from .views import HomeView, SignupView, LoginView, logoutUser, DashboardView, CourseDetailView

urlpatterns = [
    path('', HomeView, name="home"),
    path('signup/', SignupView, name="signup"),
    path('login/', LoginView, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('dashboard/', DashboardView, name="dashboard"),
    path('course-details<str:course_id>/', CourseDetailView, name="course-details"),
]
