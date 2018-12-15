from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setupwithusers import Category, Base, User, Item

engine = create_engine('sqlite:///itemcatelogwithusers1.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
#session.rollback()
session = DBSession()

# users
User1 = User(name="Ganavi", email="ganavijayaram1996@gmailcom",
             picture='https://pbs.twimg.com/profile_images'
             '/2671170543'
             '/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


User2 = User(name="Vinay Kowdle", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images'
             '/2671170543'
             '/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

# items for Italian
category1 = Category(user_id=1, name="Italian")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Caprese Salad with Pesto Sauce" +"ng",
              description="Nothing like a fresh tomato salad in summers! A great antipasto bite to start your"+
             "meal with. This combination of juicy tomatoes and mozzarella cheese salad topped with freshly made pesto"+
             " sauce is a distinct yet simple one. It offers a twist to the classic caprese salad. PRICE:Rs 250", category=category1, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Panzenella" +
             "g", description="Panzenella is a Tuscan bread salad, ideal for summer. It does not follow a particular recipe,"+
             "but the two ingredients that do not change are tomatoes and bread. This salad is great with a chilled glass of"+
             "Prosecco and lots of sunshine PRICE:Rs 550", category=category1, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Focaccia Bread ", description="Fresh dough is topped with caramelized onions, olives, tomato"+
             "slices, basil leaves, grated parmesan cheese and baked delicious! PRICE:Rs 850", category=category1, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Bruschetta", description="An antipasto dish, bruschetta has grilled bread topped with "+
             "veggies, rubbed garlic and tomato mix. A country bread sliced and topped with different toppings - the evergreen"+
             "tomato-basil and an inventive mushroom-garlic. The classic Italian starter! PRICE:Rs 150", category=category1, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item4)
session.commit()

# items for Code Spanish
category2 = Category(user_id=1, name="Spanish")
session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Croquettes ", description="It’s also a good yardstick for comparing food in Spain: the quality "+
             "of a bar-restaurant can often be judged by their ability to handle the Spanish tapa staples of croquettes or"+
             "bravas (Spanish potato chips). The traditional, scrubbed-down bars usually serve the best. PRICE:Rs 290", category=category2, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Tortilla Espanola ", description="The Spanish omlette is another beloved top Spanish food –"+
             "and everyone has an opinion on how to cook it. It’s a great starter (or meal) for breakfast, lunch and"+
             "dinner, and no doubt you’ll come across many Spanish potato omelettes during your time in Spain. Like"+
             "croquetas, you can find them in almost any bar and to varying degrees of quality and flavour. The best"+
             "ones come from slow-cooking caramalised onion and potato in olive oil, which later creates a soft-sweet"+
             "centre once egg is added and it is cooked into a thick omelette, almost like a cake. A tasty Spanish "+
             "snack you’ll see around is a wedge of omelette squeezed between bread to make a bocadillo (sandwich). PRICE:Rs 450", category=category2, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Gazpacho ", description="This zesty, chilled tomato soup has claimed space in supermarkets"+
             "and on menus around the world, but few compare to refreshing Spanish gazpacho made with full-flavoured Spanish"+
             "tomatoes. Usually eaten as an appetizer – and sometimes drunken straight from a bowl or glass – this"+
             "thick soup is made from blending a whole heap of fresh tomatoes, green peppers, cucumbers, garlic, onions, "+
             "vinegar and herbs. It’s the perfect Spanish food for summer, as well as a low calorie and healthy dish."+
             "Salmorejo is a similar Andalucian version combining pureed bread, tomatoes, garlic and vinegar – also "+
             "served cold – and sometimes varied with a bit of ham or egg slices on top. PRICE:Rs 1250", category=category2, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Cured meats", description="Jamon is ubiquitous in Spain, carved thinly"+
             "off cured legs of pork that you will see hanging in most bars and restaurants. Jamon"+
             "is a serious business and an art in Spain, with many factors in place to determine quality,"+
             "such as what the pigs are fed, the type of pig and the curing process. Jamón ibérico de bellota "+
             "is the top category, where Spanish pigs (Ibérico) are free-range and acorn-fed (bellota); other types"+
             "include Ibérico (corn-fed) or Serrano ham, which are typically cheaper. PRICE:Rs 2510", category=category2, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item4)
session.commit()

# items for  Indian
category3 = Category(user_id=1, name="Indian")
session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Butter Chicken", description="This gorgeous plate is the reason"+
             " every Punjabi takes pride in his food. Chunks of chicken marinated overnight in"+
             "yogurt and a beautiful mix of spices, served with a dollop of melting cream or"+
             "butter on top. A perfect dinner party recipe, this North-Indian style chicken"+
             "recipe is made throughout the country with equal zest. PRICE:Rs 2500", category=category3, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Bhapaa Aloo", description="A stunner of a recipe, this one"+
             "gets the Bengali flavours just right. Bhapaa is the Bengali word for steamed"+
             "and this bengali recipe is exactly what it means. The humble potato tossed"+
             "in local flavours of panch phoron (five spice powder), coconut paste and"+
             "mustard oil, steamed to perfection. You can simply say this is a vegetarian"+
             "version of Bhapaa Maach, just the fish has been replaced with baby potatoes."+
             "Simple yet satisfying!    PRICE:Rs 200", category=category3, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

# items for Japanese
category4 = Category(user_id=1, name="Japanese")
session.add(category4)
session.commit()

item1 = Item(user_id=1, name="Agedashi Tofu", description="Soaked in a sweet savory sauce, this deep-fried"+
             "Agedashi Tofu makes an impressive appetizer for your vegetarian guests.    PRICE:Rs 210", category=category4, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Yakitori", description="Transport your guests to izakaya dining (Japanese tapas)"+
             "experience with this Chicken & Scallion Yakitori dish. You can of course grill outside,"+
             "but this recipe shows how to use your oven to achieve the nicely charred meat skewers. PRICE:Rs 2500", category=category4, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

# items for Chinese
category5 = Category(user_id=1, name="Chinese")
session.add(category5)
session.commit()

item1 = Item(user_id=1, name="Dim Sums", description="Small bite-sized rounds stuffed with veggies"+
             "or meat. This essentially a Cantonese preparation. PRICE:Rs 2050", category=category5, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Hot and sour soup", description="A soup with a spicy and sour broth."+
             "It is made spicy by using red peppers or white pepper and sour with vinegar.", category=category5, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Noodles", description="One of the staples in every Chinese home,"+
             "this version is super speedy. Just bung in all your favourites and create a"+
             "masterpiece of your own. PRICE:Rs 20", category=category5, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item3)
session.commit()

# items for German
category6 = Category(user_id=2, name="German")
session.add(category6)
session.commit()

item1 = Item(user_id=2, name="Rouladen", description="This typical German food involves wrapping"+
             "thinly sliced meat – usually beef but also veal or pork – around a filling"+
             "of bacon or pork belly, chopped onions, pickles and usually mustard, and then"+
             "browned and simmered in broth (braised). The mixture changes between regions,"+
             "with some variations including minced meat. It is common to serve this dish with"+
             "gravy, dumplings, mashed potato or blaukraut (cooked red cabbage). This was once "+
             "considered a common dish using cheap meats but is now eaten at festivals, weekends"+
             "and family meals. PRICE:Rs 50", category=category6, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=2, name="Rote grütze ", description="Rote grütze is a red fruit pudding that"+
             "is a popular dessert in northern Germany. It’s made from black and red currants,"+
             "raspberries and sometimes strawberries or cherries, which are cooked in their juices"+
             "and thickened with a little cornstarch or cornflour. It’s served with cream (sahne), milk"+
             "or vanilla sauce or ice-cream. ", category=category6, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()


# items for Indonesian
category7 = Category(user_id=2, name="Indonesian")
session.add(category7)
session.commit()

item1 = Item(user_id=2, name="Nasi goreng", description="Nasi Goreng, which is “fried rice” and known as the"+
             "national dish of Indonesian. This take on Asian fried rice is often"+
             " made with sweet, thick soy sauce called kecap and garnished with acar,"+
             "pickled cucumber and carrots.", category=category7, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=2, name="Sate", description="Sate is a grilled meat dish famous"+
             "throughout Southeast-Asia. Indonesians consider it a national dish"+
             "conceived by street vendors and popularized by Arab traders.", category=category7, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

item3 = Item(user_id=2, name="Bakso", description="Bakso is a delightful dish that takes on many"+
             "forms; these meatballs are made from chicken, beef, pork or some"+
             "amorphous combination of them all. In Indonesia they classify this dish"+
             "as comfort food.", category=category7, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item4)
session.commit()

# items for DC Swiss
category8 = Category(user_id=2, name="Swiss")
session.add(category8)
session.commit()

item1 = Item(user_id=2, name="Cheese fondue", description="Cheese fondue is a great"+
             "meal with friends and perhaps one of the most iconic foods that people"+
             "relate to Switzerland. It's a dish made of melted cheese (gruyère and"+
             "emmentaler) and other ingredients, such as garlic, white wine, a little" +
             "cornflour/corn starch and often kirsch (cherry brandy), served up at the table"+
             "in a special ceramic pot called a caquelon, with a small burner underneath it to keep"+
             "the fondue at constant temperature. You spear small cubes of bread onto long-stemmed"+
             "forks and dip them into the hot cheese (taking care not to lose the bread"+
             "in the fondue)", category=category8, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()


item2 = Item(user_id=2, name="Rösti", description="Rösti is a potato dish made"+
             "by frying (or occasionally baking) flat round patties of coarsely"+
             "grated raw or parboiled (semi-cooked), seasoned potato in oil."+
             "They're crisp on the outside and soft and melting inside. Sometimes bacon,"+
             "onion, cheese – and even apple – are added to the mix. It's eaten as a side"+
             "dish to accompany fried eggs and spinach or a sausage meat called fleischkäse."+
             "It was originally eaten as a breakfast by Bern farmers but these days you'll"+
             "find it enjoyed all over the world as well as in Switzerland where it's considered"+
             "a national dish.", category=category8, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

# items for French
category9 = Category(user_id=2, name="French")
session.add(category9)
session.commit()

item1 = Item(user_id=2, name=" French Onion Soup", description="Beautifully caramelised "+
             "onions impart a nice brown colour and aroma to this classic French onion "+
             "soup. Traditionally served with slices of baguettes baked with cheese, this"+
             "soup is a winner at the dinner table.", category=category9, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=2, name="Croissants", description="A croissant is a buttery flaky"+
             "French bread roll which can be made with or without a filling. It's"+
             "slightly tedious to make but undoubtedly worth the effort.", category=category9, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()

item3 = Item(user_id=2, name="Lobster Thermidor", description="A classic French dish"+
             "where the lobster shell is stuffed with a creamy mixture of meat,"+
             "egg yolks and brandy. Top up with cheese and bake for an oven-browned"+
             "cheese crust.", category=category9, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item3)
session.commit()

# items for Thai
category10 = Category(user_id=2, name="Thai")
session.add(category10)
session.commit()

item1 = Item(user_id=2, name="Chicken Pad Thai", description="This tried and true recipe"+
             "for the world's favorite noodles will leave you craving more. The pad"+
             "thai sauce is authentic and tangy, with a true balance of"+
             "flavors. Fry some up for your loved ones and enjoy a Thai"+
             "food taste experience!", category=category10, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item1)
session.commit()

item2 = Item(user_id=2, name="", description="There's imitation satay"+
             "and then there's the real deal. This recipe has been"+
             "passed down through my husband's family (from Thailand) "+
             "for many generations and is quite simply the best I've"+
             "ever tried. Strips of chicken (or beef) are marinated"+
             "in a special Thai paste, then skewered and grilled on"+
             "the BBQ or broiled in the oven. Even your kids will love"
             "it.", category=category10, picture='https://www.google.co.in/url?'
             'sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjqg6aj94_fAhUbX30KHQ-dAnAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.delish.com%2Fcooking%2'
             'Frecipe-ideas%2Frecipes%2Fa45764%2Fspaghetti-with-sun-dried-tomatoes-sausage-and-spinach-recipe%2F&psig=AOvVaw0PKgCzLptZvbvMXYyIROIJ&ust=1544348131088563')
session.add(item2)
session.commit()


print("added items")
