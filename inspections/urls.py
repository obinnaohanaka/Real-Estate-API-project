from django.urls import path

from inspections.views.create_inspection_booking_view import (
    CreateInspectionBookingView,
)
from inspections.views.list_inspection_booking_view import (
    ListInspectionBookingView,
)
from inspections.views.update_inspection_status_view import (
    UpdateInspectionStatusView,
)

urlpatterns = [
    path(
        "",
        ListInspectionBookingView.as_view(),
        name="list-inspections",
    ),

    path(
        "book/",
        CreateInspectionBookingView.as_view(),
        name="book-inspection",
    ),
    
    path(
        "<int:pk>/status/",
        UpdateInspectionStatusView.as_view(),
        name="update-inspection-status",
    ),
]