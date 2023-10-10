# git_finder
This application provides a user-friendly way to retrieve and open repositories of a GitHub user using their username.

Here's how it works:
1. The application has a graphical user interface (GUI) built using the tkinter module in Python.
2. It uses the PIL module to open and display an image of the GitHub logo as the application icon.
3. The application has an input field where you can enter a GitHub username.
4. There's a "find out..." button that triggers a function called getrepo() when clicked.
5. Inside the getrepo() function, it retrieves the username entered in the input field and constructs a URL to the GitHub API to fetch the user's repositories.
6. It then sends a GET request to the API using the requests module and checks the response status code.
7. If the request is successful (status code 200), it retrieves the repositories data from the response in JSON format.
8. The application clears the text field and displays each repository name followed by its URL in a new line.
9. Each URL is set as a clickable link using the tkinter Text widget, and when clicked, it opens the URL in a web browser using the webbrowser module.
10. If the request is unsuccessful, it displays an error message with the corresponding status code.
11. The GUI layout is organized using frames and widgets, and the application window is sized and configured appropriately.

