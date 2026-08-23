# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]

#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(
#                 {"detail": "Successfully logged out."},
#                 status=status.HTTP_205_RESET_CONTENT,
#             )

#         except Exception:
#             return Response(
#                 {"detail": "Invalid or expired refresh token."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken

# from accounts.serializers.logout_serializer import LogoutSerializer


# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = LogoutSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         try:
#             refresh_token = serializer.validated_data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(
#                 {"detail": "Successfully logged out."},
#                 status=status.HTTP_205_RESET_CONTENT,
#             )

#         except Exception:
#             return Response(
#                 {"detail": "Invalid or expired refresh token."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )



from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers.logout_serializer import LogoutSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"detail": "Successfully logged out."},
                status=status.HTTP_205_RESET_CONTENT,
            )

        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )