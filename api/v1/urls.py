from api.v1.views.property_details_view import PropertyDetailsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("property_details", PropertyDetailsView, r"property_details")

urlpatterns = router.urls