# TESTING

For a proper conclusion to this project several tests were performed.

## 🚀 TABLE OF CONTENTS

* [RESPONSIVENESS TESTING](#responsiveness-testing)
* [BROWSER COMPABILITY TESTING](#browser-compability-testing)
* [BUGS RESOLVED AND UNRESOLVED](#bugs-resolved-and-unresolved)
* [LIGHTHOUSE TESTING OUTCOMES](#lighthouse-testing-outcomes)
* [CODE VALIDATION](#code-validation)
* [USER STORIES TESTING](#user-stories-testing)
* [FEATURES TESTING](#features-testing)
* [AUTOMATED TESTING](#automated-testing)
* [TEST CASE](#test-case)

Return back to the [README.md](README.md) file.

- - -

## RESPONSIVENESS TESTING

The deployed application was tested on multiple devices to check for responsiveness issues. (Which devices, issues)
It works as expected according to the wireframes.
### Mobile

![]()

### Tablet

![]()

### Laptop

![]()

### Desktop

![]()

- - -

## BROWSER COMPABILITY TESTING

The deployed project was tested on multiple browsers to check for compatibility issues. (Work as expected?)
### Chrome

![]()

### Firefox

![]()

### Edge

![]()

### Safari

![]()



- - -

## BUGS RESOLVED AND UNRESOLVED 
☠️ The issues listed in the table below were indentified during the development of the project.

|N.| Issue |  Action | Status | 
|:---|:--- |:--- |:--- |
|01| Table django_session don't exists | Command: python manage.py migrate sessions | Closed | 
|02 | After migration to codeanywhere, Error: pg_config executable not found | install psycopg2-binary | Closed |
|03 | After migration to codeanywhere, the app didn't run | Create virtual enviroment | Closed |
|04 | Sticky footer overlapping content | Remove class fixed-sm-bottom; add display: flex, direction: column and min-height:100vh to body and margin-top:auto to footer | Closed |
|05 | Bullets in nav list | Edit default in CSS nav ul {list-style-type: none;} | Closed |
|06 | Dropdown menu doesn't display own profile | Change the user.profile.pk to request.user.profile.pk | Closed | 
|07 | Profile_pic doesn't display correctly | Edit templates, change bootstrap classes | Closed |
|08 | Admin couldn't delete post or comment from other users | Edit the template and view adding request.user.is_superuser |
|09 | Inpunt form doesn't clean after submit | Add class form-control | Closed |
|10 | Default profile_pic doesn't display | Add boolean to templates | Closed |
|11 | Reply comment icon button doesn't work. Parent_id was not found. | Remove '' from argument in the function. | Closed |
|12 | Default profile picture doesn't be displayed at followers_list. | Edit the template followers_list with boolean | Closed | 
|13 | ConnectionRefusedError at /accounts/password/reset/ | Google and Gitpod don't see eye-to-eye and will not send emails from a Google SMPT account. Use outlook account to send email to reset password, but got Error 500 at Heroku, then changed to a new google account, turn on the 2-Step Verification and use the App Password.| Closed |
|14 | Skip collestactic at Heroky during deployment | Run the command **python manage.py collectstatic** then deploy the project again. | Closed|
|15 | Couldn't test the application using a free version of Elephant as a database | Create a temporary database to test the application | Closed |
|16 | Post and Comment form doesn't clear after it's submitted | Call the empty form after save the content posted | Closed |
|17 | After changed the password redirects to change password page | Add a path with reverse_lazy to overwrite django allauth | Closed |
|18 | Post author couldn't delete comments in own post | Edit view and template adding if request.user == post.author. | Closed |
|19 | The table of contents on the README.md an TESTING.md doesn't work due to emojis in titles. | Remove all emojis from titles. | Closed|
|20 | NameError: name 'settings' is not defined | Remove the static from urls | Closed |

There are no remaining bugs.

- - -

## LIGHTHOUSE TESTING OUTCOMES

The deployed project was tested using the Lighthouse Audit tool to check for any major issues. The results for each page are listed bellow.

**Best Practices**: Displays images with incorrect aspect ratio - this will happen due to the uploading of photos by the user.

Some tests were made using DevTool with Google Chrome, but it was very slow and other tests were made with Microsoft Edge, where the language was German. (Leistung = Performance, Barrierefreiheit = Accessibility)


- Home (Landing page - not Logged in)

![Home](documentation/images/l-home.png)

- Sing Up

![Sing Up](documentation/images/l-signup.png)

- Sing In

![Sing In](documentation/images/l-signin.png)

- Sing Out

![Sing Out](documentation/images/l-signout.png)

- Reset Password 

![Reset Password](documentation/images/l-password-reset.png)


- Reset Password Done

![Reset Password Done](documentation/images/l-password-reset-done.png)

- Change Password

![Change Password](documentation/images/l-password-change.png)

- Home (Main Feed - Logged in)

![Home - Main Feed - Logged in](documentation/images/l-main-feed.png)

- Following

![Following](documentation/images/l-following.png)

- Post Detail

![Post Detail](documentation/images/l-post-detail.png)

- Edit post

![Edit post](documentation/images/l-post-edit.png)

- Delete post

![Delete post](documentation/images/l-post-delete.png)

- Edit comment

![Edit comment](documentation/images/l-comment-edit.png)

- Delete comment

![Delete comment](documentation/images/l-comment-delete.png)

- Users

![Users](documentation/images/l-users.png)

- Search

Valid query:

![Search](documentation/images/l-search.png)

No user found:

![Search](documentation/images/l-search-no-one.png)

- Profile

![Profile](documentation/images/l-profile.png)

- Profile Update

![Profile Update](documentation/images/l-profile-update.png)

- Followers

![Followers](documentation/images/l-followers.png)


- - -

## CODE VALIDATION

### HTML

The [HTML W3C Validator](https://validator.w3.org/) to validate all HTML files.
In order to properly validate the HTML pages with Jinja syntax, the steps are followed for each file:

- Navigate to the deployed application using Google Chrome,
- Right-click anywhere on the page, and select View Page Source.
- Copy the entire "compiled" code, without any Jinja syntax., and use the validate by input method.

The result for each page are listed bellow:

- Home (Landing)

First test:
**Warning**: The type attribute is unnecessary for JavaScript resources. - Removed from script.

Second test:

![HTML Validation - Home](documentation/images/v-html-home.png)

- Sing Up

![HTML Validation - Singup](documentation/images/v-html-signup.png)

- Sing In

![HTML Validation - Singin](documentation/images/v-html-signin.png)

- Sing Out

![HTML Validation - Singout](documentation/images/v-html-signout.png)

The error message was ignored, because the the `aria-controls` identifies an element in the same document whose contents are controlled by the current element.

![HTML Validation - Singout](documentation/images/v-html-signout-id.png)

- Reset Password

First test:

Error: Attribute mt-2 not allowed on element p at this point. - Add the missed `class=" "`.

Second test:

![HTML Validation - Password Reset](documentation/images/v-html-password-reset.png)

- Reset Password Done

![HTML Validation - Password Reset Done](documentation/images/v-html-password-reset-done.png)


- Home (Main Feed - Logged in)

![HTML Validation - Main Feed](documentation/images/v-html-main-feed.png)

- Following

First test:

![HTML Validation - Following Feed](documentation/images/v-html-following-1.png)

"Picture uploaded" was added as an alt attribute to uploaded image by user.
Second test:
![HTML Validation - Following Feed](documentation/images/v-html-following-2.png)

- Post Detail

![HTML Validation - Post Detail](documentation/images/v-html-post-detail.png)

- Edit post

![HTML Validation - Edit Post](documentation/images/v-html-post-edit.png)

- Delete post

![HTML Validation - Delete Post](documentation/images/v-html-post-delete.png)

- Edit comment

![HTML Validation - Edit Comment](documentation/images/v-html-comment-edit.png)

- Delete comment

![HTML Validation - Delete Comment](documentation/images/v-html-comment-delete.png)

- Users

First test:

![HTML Validation - Users](documentation/images/v-html-users-1.png)

The double escape `&amp;amp;` was added.

Second test:

![HTML Validation - Users](documentation/images/v-html-users-2.png)

- Search

First test:

![HTML Validation - Search](documentation/images/v-html-search.png)
The double escape `&amp;amp;` was added.
Second test:
![HTML Validation - ](documentation/images/v-html-search-2.png)

- Profile

First test:

![HTML Validation - Profile](documentation/images/v-html-profile.png)

 - `<h3/>` written in the right place.

Second test:

![HTML Validation - Profile](documentation/images/v-html-profile-2.png)

- Profile Update

![HTML Validation - Profile Update](documentation/images/v-html-profile-update.png)

- Change Password

First test:

![HTML Validation - Change Password](documentation/images/v-html-password-change-error.png)

Div was removed.

Second test:

![HTML Validation - Change Password](documentation/images/v-html-password-change.png)

- Followers

![HTML Validation - Followers](documentation/images/v-html-followers.png)

- Error 403

![HTML Validation - Error 403](documentation/images/v-html-error-403.png)

- Error 404

![HTML Validation - Error 404](documentation/images/v-html-error-404.png)


- Error 500

![HTML Validation - Error 500](documentation/images/v-html-error-500.png)
- - - 


### CSS

The [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS file.

| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![style.css](documentation/images/v-css.png) | ![style.css warning](documentation/images/v-css-warning.png) |

- - - 

### JAVASCRIPT

The [JShint Validator](https://jshint.com/) was used to validate the JavaScript file.

| File | Screenshot | Notes |
| --- | --- | --- |
| titbit.js | ![screenshot](documentation/images/v-javascript.png) | Unused variables: commentReply Toggle, showNotifications and removeNotifications |


- - - 


### PYTHON

The [Code Institute Python Linter](https://pep8ci.herokuapp.com)was used to validate all Python files.

#### Network project

- Settings.py

![Settings](documentation/images/v-network-settings.png)

- urls.py (main)

![Urls](documentation/images/v-network-urls.png)

- views.py

![Views](documentation/images/v-network-views.png)

#### Home app

- urls.py 

![Urls](documentation/images/v-home-urls.png)

- views.py

![Views](documentation/images/v-home-views.png)

- custom_tags.py

![Custom Tags](documentation/images/v-home-custom-tags.png)

#### Titbit app

- admin.py

![Admin](documentation/images/v-titbit-admin.png)

- forms.py

![Forms](documentation/images/v-titbit-forms.png)

- models.py

![Models](documentation/images/v-titbit-models.png)

- tests.py

![Tests](documentation/images/v-titbit-tests.png)

- urls.py

![Urls](documentation/images/v-titbit-urls.png)

- views.py

![Views](documentation/images/v-titbit-views.png)


- - -

## USER STORIES TESTING

The User Stories testing  were listed bellow:


- - -

## FEATURES TESTING

- - -

## AUTOMATED TESTING

The Django's Built-in Unit Testing Framework was used to test the application functionality on the project without errors.
To perform the test the following step was used:
- In the terminal type the command:

```bash
python3 manage.py test
```


- - -

## TEST CASE

A test case were written to proof the post feature and the delete post. A creation of a temporary database was needed.
Ran 2 tests without issues.

![Teste Case](documentation/images/test-case.png)






