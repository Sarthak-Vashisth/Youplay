from . import masterconf
import os


class CommonUtils():

	def divide_store_file ( self , request ) :
		filehandle = request.FILES['file']
		filehandle_name = request.FILES['file'].name
		input_filepath = os.path.join ( masterconf.input_file_path , filehandle_name )
		with open ( input_filepath , 'wb+' ) as fout :
			# Iterate through the chunks.
			for chunk in filehandle.chunks ( ) :
				fout.write ( chunk )
			fout.close ( )
		return input_filepath

	def validate_individual_list_request(self,request_data):
		params = masterconf.input_params_individual_videos
		status_flag = False
		for param in params:
			if param not in request_data.keys():
				status_flag = False
				break
			else:
				status_flag = True
		return status_flag
