import re

disease_dic = {
    'Apple___Apple_scab': """ <b>Crop</b>: Apple <br/>Disease: Apple Scab<br/>
        <br/> Cause of disease:
        <br/><br/> 1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
        <br/> 2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.
        <br/><br/> How to prevent/cure the disease <br/>
        <br/>1. Choose resistant varieties when possible.
        <br/>2. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring
        
        <br/>3. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
        <br/>4. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores.""",
    }

# extract the text
text = re.sub(r'<[^<]+?>', '', disease_dic['Apple___Apple_scab'])

# print the text
print(text)
