# from rest_framework.parsers import JSONParser
# from rest_framework.views import APIView
#
# import requests
# import xmltodict
# from dicttoxml import dicttoxml
#
#
#
# def get_coordinates(address,output_format):
#     key = 'AIzaSyCDD3KvY2DDzEFEL-NZ_LKIWXr86EF_EUw'
#     end_point = f"https://maps.googleapis.com/maps/api/geocode/{output_format}?address={address}&key={key}"
#     data={}
#     url_response = requests.get(url=end_point)
#     if output_format == 'json':
#         latlng = url_response.json()['results'][0]['geometry']['location']
#         data.update({'coordinate':latlng})
#         data.update({'address':address})
#         return data
#     else:
#         value = xmltodict.parse(url_response.content)
#         latlng = value['GeocodeResponse']['result']['geometry']['location']
#         data.update({'coordinate': latlng})
#         data.update({'address': address})
#         xml = dicttoxml(data,attr_type=False)
#         return xml
#
#
#
#
#
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         print(data)