from django.shortcuts import render
import openai
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.


@api_view(['POST'])
def generate_listing_description(request):
    openai.api_key = "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"
    model_id = 'gpt-3.5-turbo'
    print(request)
    if request.method == 'POST':
        property_type = request.data['propertyType']
        sale_type = request.data['saleType']
        bedrooms = request.data['bedrooms']
        bathrooms =request.data['bathrooms']
        parking_spaces = request.data['parkingSpaces']
        square_footage = request.data['squareFootage']
        address = request.data['address']
        max_word_count = request.data['maxWordCount']
        house_details = request.data['houseDetails']
        community_details = request.data['communityDetails']

        # Construct the prompt for GPT-3
        prompt = f"Property Type: {property_type}\n"
        prompt += f"Transaction Type: {sale_type}\n"
        prompt += f"Bedrooms: {bedrooms}\n"
        prompt += f"Bathrooms: {bathrooms}\n"
        prompt += f"Square Footage: {square_footage}\n"
        prompt += f"Address: {address}\n"
        prompt += f"Max Word Count: {max_word_count}\n"
        prompt += f"House Details: {house_details}\n"
        prompt += f"Community Details: {community_details}\n\n"
        prompt += "Generate a property description which would entice people to want to buy the property and live in it:\n"

        # Generate the real estate listing description using GPT-3
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',messages=[{"role":"user","content":prompt}]
        )
          
        listing_description = response
        print(listing_description)
        # Return the generated listing description as JSON response
        return JsonResponse({'listing_description': listing_description})

    # Handle non-POST requests or other errors
    return JsonResponse({'error': 'Invalid request'})
