from django.urls import path

from inquiries.views.list_received_inquiries_view import ListReceivedInquiriesView
from inquiries.views.list_sent_inquiries_view import ListSentInquiriesView
from inquiries.views.send_inquiry_view import SendInquiryView
from inquiries.views.update_inquiry_status_view import (
    UpdateInquiryStatusView,
)

urlpatterns = [
    path(
        "<int:listing_id>/send/",
        SendInquiryView.as_view(),
        name="send-inquiry",
    ),

    path(
        "sent/",
        ListSentInquiriesView.as_view(),
        name="sent-inquiries",
    ),

    path(
        "received/",
        ListReceivedInquiriesView.as_view(),
        name="received-inquiries",
    ),

    path(
        "<int:inquiry_id>/status/",
        UpdateInquiryStatusView.as_view(),
        name="update-inquiry-status",
    ),
]