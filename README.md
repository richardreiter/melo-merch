# Melo Merch

[Melo Merch](https://github.com/richardreiter/melo-merch) is an online Business-to-Consumer (B2C) e-commerce website dedicated to selling streetwear fashion apparel and skater products such as tees, hoodies, shorts, hats and skateboards.

![Responsive Melo Merch](media/docs/mm-responsiveness.png)

Visit the live site [here.](https://melo-merch.herokuapp.com/)

## UX (User Experience)

### Project Goals

- Create a fully functional e-commerce website to allow users to purchase streetwear fashion products - including features (but not limited to) such as easy payment gateway, authentication system, search and filter functionality, high quality product images, clear product descriptions, ratings, shopping cart and a single payment system.

### Target Audience

- Anyone who is into streetwear fashion and skateboarding.
- People looking to purchase a present for someone who's into streetwear/skateboarding.

### User Stories

Agile methodology tool:

  - GitHub Projects was used to create and [manage a Kanban board](https://github.com/richardreiter/melo-merch/projects/1), for planning and implementing this project's functionalities.
![Kanban Board Melo Merch](media/docs/mm-kanban-board.png)

- As a Site User I can register for an account so that I have my personal account information.
- As a site user I can login/logout of my account so that I have access to my account details.
- As a Site User I can recover my password in case I forget it so that I can regain access to my account.
- As a Site User I can receive an email confirmation after registration so that I can confirm my account creation.
- As a Site User I can personalise the user profile so that I can view my order history/confirmations/save my payment information.
- As a Shopper I can browse a list of products so that I can pick some I'd like to buy.
- As a Shopper I can view a certain product's details so that I see a full description, ratings, picture, sizes.
- As a Shopper I can easily identify any sales so that I can save some money.
- As a Shopper I can see my bag total anytime so that I can be within budget.
- As a Shopper I can view a category of a product so that I can easily find a product I'm interested in without having to browse too much.
- As a Shopper I can sort the products' list so that I can sort products by specific filters.
- As a Shopper I can sort more than one category so that I can better tailor the filters to my needs.
- As a Shopper I can search/query a product so that I can find a specific product easily.
- As a Shopper I can see the result of my query so that I can find out if the shop stocks the product I'm looking for.
- As a Shopper I can pick size/quantity of product when buying it so that I don't accidentally select the wrong size/quantity.
- As a Shopper I can see the items in my cart so that I can have control over my spending.
- As a Shopper I can update the amount of items in my cart so that I can make adjustments before checking out.
- As a Shopper I can put my card details with ease so that I can quickly checkout.
- As a Shopper I can safely input my details so that my details are secure.
- As a Shopper I can view my order and confirmation of the order after checking out so that I can double-check the order is correct.
- As a Shopper I can get an email confirmation of my order so that I can keep for my records.
- As a Site Admin I can add a product so that I can keep the inventory updated with new merch.
- As a Site Admin I can update a product so that I can change the price/image/description/name.
- As a Site Admin I can delete a product so that I can delete items which I no longer wish to sell.
- As a Site User I can see a custom 404 page so that I'm not confused on why I didn't land on the page I had intended to.
- As a Shopper/Potential Shopper I can find a contact page so that I can easily contact the shop with any questions/concerns.
- As a Shopper I can subscribe to a newsletter so that I can keep up to date with new collections, sales, discounts.
- As a Shop Owner I can link a privacy policy so that shoppers know how their data is collected and processed.
- As a Site Owner I can improve my SEO so that I improve my search engine ranking.
- As a Shop Owner I can create a FB business page so that I can gain more traction from socials.
- As a Shopper I can see a FAQ page so that I can find the most frequently asked questions, without having to contact the shop.
- As a Shopper I can see an about page from the shop so that I can learn more about its story, and gain trust from the brand.
- As a Shopper I can add a product to a wish list so that I can purchase it at a later stage.
- As a Shopper I can leave a review of a product so that other users can see my opinion.

### Wireframes

The mockups below were done with the help of Balsamiq (for both desktop and mobile screens), these were useful to help visualise the project.

- Desktop:
  - Home page
  ![Home Desktop Mockup](media/docs/desk-wireframe-home.png)
  - Products page 
  ![Products Desktop Mockup](media/docs/desk-wireframe-products.png)
  - Product Detail page
  ![Products Desktop Mockup](media/docs/desk-wireframe-product-detail.png)
  - Cart page
  ![Cart Desktop Mockup](media/docs/desk-wireframe-cart.png)
  - Checkout page
  ![Checkout Desktop Mockup](media/docs/desk-wireframe-checkout.png)
  - Sign Up page
  ![Sign Up Desktop Mockup](media/docs/desk-wireframe-signup.png)
  - Login page
  ![Login Desktop Mockup](media/docs/desk-wireframe-login.png)
  - About page
  ![About Desktop Mockup](media/docs/desk-wireframe-about.png)
  - Subscribe page
  ![Subscribe Desktop Mockup](media/docs/desk-wireframe-subscribe.png)
  - FAQ page
  ![FAQ Desktop Mockup](media/docs/desk-wireframe-faq.png)
  - Contact page
  ![Contact Desktop Mockup](media/docs/desk-wireframe-contact.png)

- Mobile:
  - Home page
  ![Home Mobile Mockup](media/docs/mobile-wireframe-home.png)
  - Products page 
  ![Products Mobile Mockup](media/docs/mobile-wireframe-products.png)
  - Cart page
  ![Cart Mobile Mockup](media/docs/mobile-wireframe-cart.png)
  - Sign Up page
  ![Sign Up Mobile Mockup](media/docs/mobile-wireframe-signup.png)
  - Login page
  ![Login Mobile Mockup](media/docs/mobile-wireframe-login.png)
  - About page
  ![About Mobile Mockup](media/docs/mobile-wireframe-about.png)
  - Subscribe page
  ![Subscribe Mobile Mockup](media/docs/mobile-wireframe-subscribe.png)
  - FAQ page
  ![FAQ Mobile Mockup](media/docs/mobile-wireframe-faq.png)
  - Contact page
  ![Contact Mobile Mockup](media/docs/mobile-wireframe-contact.png)

The database schema was generated with [django-extensions](https://django-extensions.readthedocs.io/en/latest/index.html) [Graph models.](https://django-extensions.readthedocs.io/en/latest/graph_models.html)

- Database Schema
  ![Database Schema](media/docs/mm-db-schema.png)

### Design

- The colour scheme is gold old fashion/classic black & white - [contrast passes a11y validation.](https://color.a11y.com/)
![Color scheme contrast validation](media/docs/a11y-color-contrast.png)

- [Google Fonts](https://fonts.google.com/) was used for the website's font. The Playfair Display font was used as it gives an air of elegance and it's a stylish font.

## Features

### Existing Features

- __Navigation Bar__

  - Navigation is a fully responsive feature on all pages (with different versions user's role dependant and whether the user is logged in/out), it includes links on the site's Logo (displaying to the left within the bar), Search Bar in the middle, My Account and Shopping car to the right. All Products, Clothing, Skateboards, About, Subscribe, FAQ and Contact Pages are located under the search bar. The Register and Login pages are located in a submenu upon clicking My Account (the 'Product Management' and "Mail Newsletter" pages/nav links only show up for superusers).
    ![Navigation Bar Superuser Logged In](media/docs/mm-nav-logged-in-admin.png)
  - The Logout nav link shows up (and both Register/Login nav links disappear) once the user has successfully registered/logged in.
    ![Navigation Bar Logged In](media/docs/mm-nav-logged-in-user.png)
    ![Navigation Bar User Logged Out](media/docs/mm-nav-logged-out.png)
  - The navigation looks the same in each page to allow for easy navigation (without the user having to use the ‘back’ button), taking the user through a logical journey.
  - This section makes it easy for the user to learn more about the site's different sections and contents.
  - The search box makes it easy for the shopper/user to search fo a specific item.
    ![Search Box](media/docs/mm-search-box.png)
  - My Account icon expands upon click with a sub-menu.
    ![My Account icon](media/docs/mm-my-account-icon.png)
  - Cart icon reflects on the current state of how much the shopper will spend, if the shopper clicks on the icon, it will bring them to the Cart Page.
    ![Cart icon](media/docs/mm-cart-icon.png)
  - All Products nav link expands upon click with a sub-menu, shoppers are able to see all products sorted by price, rating, category.
    ![All Products Nav](media/docs/mm-nav-all-products.png)
  - Clothing nav link expands upon click with a sub-menu, shoppers are able to see all clothing apparel sorted by their categories (tees, hoodies, shorts, hats).
    ![Clothing Nav](media/docs/mm-nav-clothing.png)
  - Skateboards nav link expands upon click with a sub-menu, shoppers are able to see all skateboards sorted by their categories (penny boards, regular boards, long boards).
    ![Clothing Nav](media/docs/mm-nav-skateboards.png)

- __Free Delivery Banner__

  - The Free Delivery Banner is there to entice shoppers to purchase more than €50 in order to get free delivery.
    ![Free Delivery Banner](media/docs/mm-free-delivery-banner.png)

- __CTA - Call to Action button__

  - The Shop Now button is there to entice shoppers to take the action of shopping.
    ![CTA](media/docs/mm-cta.png)

- __Footer__

  - The footer area consists of a link to the site's Privacy Policy and three social links (Facebook, Instagram and Twitter - all of them, if clicked, open on a separate tab).
  - Like the navigation section, the footer looks the same on each page (and features on all of the pages) to allow for easy navigation, taking the user through a logical journey.

![Footer](media/docs/mm-footer.png)

### Features Left to Implement

## Technologies Used

### Languages Used

### Frameworks, Libraries & Programs Used

## Testing

### Testing User Stories

### Validator Testing

### Google Lighthouse

### Color Contrast Accessibility Checker

### Responsive Testing

### Device Testing

### Browser Testing

### Known Bugs

## Deployment

### Deploying on Heroku

### Final Deployment on Heroku

### Forking the Repository

### Creating a Clone

## Credits 

### Content

### Media

### Other