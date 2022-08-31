from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from .serializers import *


@api_view(['POST'])
def element_import(request):

    serializers_dict = {"Attribute": AttributeSerializer, "AttributeValue": AttributeValueSerializer,
                        "AttributeName": AttributeNameSerializer, "Image": ImageSerializer,
                        "Product": ProductSerializer, "ProductAttributes": ProductAttributesSerializer,
                        "Catalog": CatalogSerializer, "ProductImage": ProductImageSerializer}


    # if only one JSON object is passed make a list from it
    if type(request.data) == dict:
        json_list = [request.data]
    elif type(request.data) == list:
        json_list = request.data
    else:
        # can pass only dictionary or list of dictionaries
        return Response(status=status.HTTP_403_FORBIDDEN)

    errors = []


    for element in json_list:

        try:
            element_name = list(element.keys())[0]
            element_data = list(element.values())[0]
        except (IndexError, AttributeError) as e:
            return Response({"Response" : "Wrong Json format"}, status=status.HTTP_400_BAD_REQUEST)

        # get corresponding serializer
        try:
            serializer = serializers_dict[element_name](data=element_data)
        except KeyError:
            return Response({"Response" : 'Element {} does not exit'.format(element_name)}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                errors.append(serializer.errors)

        else:
            errors.append(serializer.errors)


    if not errors:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({"Errors raised:": errors},status=status.HTTP_202_ACCEPTED)




@api_view(['GET'])
def detail_element(request, element_name: str, element_id: int = None):
    # maybe element_name needs to be put to lowercase

    models_dict = {"Attribute": Attribute, "AttributeValue": AttributeValue, "AttributeName": AttributeName,
                   "Image": Image, "Product": Product, "ProductAttributes": ProductAttributes, "Catalog": Catalog,
                   "ProductImage": ProductImage}
    
    serializers_dict = {"Attribute": AttributeSerializer, "AttributeValue": AttributeValueSerializer,
                        "AttributeName": AttributeNameSerializer, "Image": ImageSerializer,
                        "Product": ProductSerializer, "ProductAttributes": ProductAttributesSerializer,
                        "Catalog": CatalogSerializer, "ProductImage": ProductImageSerializer}


    try:
        model = models_dict[element_name]
        serializer = serializers_dict[element_name]
    except KeyError:
        return Response({"Response" : 'Element {} does not exit'.format(element_name)}, status=status.HTTP_400_BAD_REQUEST)


    # if element id is passed return the exact element, else return whole table
    if element_id is not None:
        try:
            elements = model.objects.get(pk = element_id)

        except ObjectDoesNotExist:
            return Response({"Response" : 'Element {} with id {} does not exit'.format(element_name,element_id)},
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer(elements,many=False).data

    else:
        elements = model.objects.all()
        data = serializer(elements,many=True).data


    return Response(data, status=status.HTTP_200_OK)



@api_view(['GET'])
def reset_db(request):
    """ Deletes all tables in DB but does not reset it completely
        (for example ID auto increment is not reseted)
    """
    Catalog.objects.all().delete()
    ProductAttributes.objects.all().delete()
    ProductImage.objects.all().delete()
    Product.objects.all().delete()
    Attribute.objects.all().delete()
    AttributeValue.objects.all().delete()
    AttributeName.objects.all().delete()
    Image.objects.all().delete()





    return Response({"Response": "Database was reseted"}, status=status.HTTP_200_OK)
