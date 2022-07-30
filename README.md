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

- __Products Page__

  - The Products Page features a sort by box where the shopper can sort products by Price (low to high), Price (high to low), Rating (low to high), Rating (high to low), Name (A-Z), Name (Z-A), Category (A-Z), Category (Z-A).
  - Users are able to see the products details', such as photo, name, price, category, rating, description.
  - If a user clicks on a photo it brings the user to that Product's Detail Page.
  - A back to top arrow up button can be found at the bottom right of the page.

![Products Page](media/docs/mm-products-page.png)

- __Product Detail Page__

  - The Product Detail Page features its product's image (which fully opens in a new tab upon click), name, price, category, size (if product has one), if it's limited edition or not, rating, description.
  - Users are able to click on the input box's -/+ buttons to choose the quantity of the product they wish to add to their cart.

![Product Detail Page](media/docs/mm-product-detail-page.png)

- __Cart Page__

  - The Cart Page features all the products which are currently in the cart, their images, names, sizes, sku, price, quantity, subtotal, cart total, delivery charge, grand total.
  - Users are able to click on the input box's -/+ buttons to change the number of a certain product and also update/remove them from their cart if they wish to.
  - Shoppers can click on the Secure Checkout button to head to the Checkout Page.

![Cart Page](media/docs/mm-cart-page.png)

- __Checkout Page__

  - The Checkout Page features the order summary to the right.
  - A form to the left which users need to fill out with their personal details, delivery address and card payment information, in order to complete their order.
  - If the shopper hasn't got an account they can create one or login to save their personal details.
  - The user can click on the Adjust cart button if they wish to make any last minute amendments.
  - If the user clicks on the Complete Order button they are redirected to the Checkout Success Page.

![Checkout Page](media/docs/mm-checkout-page.png)

- __Checkout Success Page__

  - The Checkout Success Page features the successful order info and delivery details.
  - Shoppers are able to click on a CTA button at the bottom of the page to check the shop's tees.

![Checkout Success Page](media/docs/mm-checkout-success-page.png)

- __Profile Page__

  - If the shopper is registered and logged in, they are able to access the Profile Page, which features the user's Default Delivery Information (where they can update).
  - Shoppers are also able to see their order history information such as order number (also click on it), date, items and the total.

![My Profile Page](media/docs/mm-profile-page.png)

- __About Page__

  - The About Page features a bit of the shop's history/mission/ethos.

![About Page](media/docs/mm-about-page.png)

- __Subscribe Page__

  - Shoppers are able to subscribe to the website's newsletter in order to receive stay up-to-date with latest merch drops, collections, sales and discounts.
  - Email validation is in place, and once a user fills out their email and click on the subscribe button, a success toast message comes up, and their email is saved to the database.

![Subscribe Page](media/docs/mm-subscribe-page.png)

- __Mail Newsletter Page__

  - **Only superusers** are able to view this page, where they are able to mail a newsletter straight from the frontend (or backend) to their subscriber's list saved in the database.
  - Once a message is sent it is also recorded to the database.

![Mail Newsletter Page](media/docs/mm-su-mail-newsletter-pg.png)

- __Product Management Page__

  - **Only superusers** are able to view this page, where they are able to add new products to the site straight from the frontend via a form.

![Product Management Page](media/docs/mm-su-product-management-pg.png)

- __FAQ Page__

  - With the shopper's most frequently asked questions, it features an accordion (collapsible content), if the shopper clicks on a certain question it expands/collapes it.

![FAQ Page](media/docs/mm-faq-page.png)

- __Contact Page__

  - Shoppers are able to contact the shop in case they have any questions/feedback/concerns.
  - Once the form is submitted it records to the database.

![Contact Page](media/docs/mm-contact-page.png)

### Features Left to Implement

- __Wish list__

  - Implementing a wish list option would be beneficial for the Melo Merch users, as they would be able to save products that they are keen on buying at a later stage.

- __Testimonial__

  - Implementing a product testimonial option would be valuable for the shop users, as it could help them make learn more about possible purchases, and gain more trust within the website and the Melo Merch brand itself.

## Technologies Used

### Languages Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python3](https://developer.mozilla.org/en-US/docs/Glossary/Python)

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/)
  - Balsamiq was used to make desktop/mobile mockups in order to visualise the project.
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap template.
- [Amazon S3](https://aws.amazon.com/s3/)
  - Amazon Simple Storage Service was used to store the project's static files such as media, CSS and JavaScript.
- [Django](https://www.djangoproject.com/)
  - Django was used to build the app.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html/)
  - Django allauth for account management.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Django Crispy Forms for rendering elegant DRY forms.
- [Font Awesome](https://fontawesome.com/)
  - Font Awesome was used to add icons to improve the design of the website.
- [Git](https://git-scm.com/) & [Gitpod](https://gitpod.io/)
  - Git was used for version control via the Gitpod terminal in order to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - GitHub was used for version control.
- [Google Fonts](https://fonts.google.com/)
  - Google Fonts was used to import the font which is used on the website.
- [Heroku](https://heroku.com/)
  - Heroku was used for hosting and deploying the application.
- [Django-extensions](https://django-extensions.readthedocs.io/en/latest/index.html)
   - The database schema was generated with [django-extensions](https://django-extensions.readthedocs.io/en/latest/index.html) [Graph models.](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
- [Django-pandas](https://pypi.org/project/django-pandas/)
  - Pandas was used to help manipulate data to mail the newsletters to the site's subscribers.
- [PostgreSQL](https://www.postgresql.org/)
  - PostgreSQL for database management.
- [Stripe](https://stripe.com/ie)
  - Stripe for the payments infrastructure.

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