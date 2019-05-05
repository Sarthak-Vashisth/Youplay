from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .Controller import individual_videos_controller
from Common import common_utils




class CreateAndPlayPlaylist(APIView):

	#authentication_classes = (JSONWebTokenAuthentication,)
	#parser_class = (MultiPartParser, FormParser,)
	#renderer_classes = (JSONRenderer,)
	#permission_classes = (IsAuthenticated,)

	def post(self,request,format=None):
		common_obj = common_utils.CommonUtils()
		post_params = request.POST
		print('post_params ::: ',post_params)
		input_file_path = common_obj.divide_store_file(request)
		check_req = common_obj.validate_individual_list_request(post_params)
		print('check_req :: ',check_req)
		if check_req:
			key = request.POST['key']
			video_obj = individual_videos_controller.CreateAndPlayController()   
			video_list = video_obj.create_video_list(input_file_path)
			print('video_list :: ',video_list)
			video_obj.playlist(video_list,key)
			return Response(status=status.HTTP_201_CREATED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

