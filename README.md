
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">


<h1 align="center">Remote File Management Software</h1>

  <p align="center">
    A remote file management software is a computer program that allows users to manage and access their files remotely from a computer or other device over a network or the internet.
    <br />
    <a href="https://rfms.pythonanywhere.com"><strong>Demo »</strong></a>
    <br />
    <br />
    <!--
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
-->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#implementation">Implementation</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

The new remote file management software is an innovative solution that offers advanced file organization, server-side compression, and scalability. It allows users to efficiently manage their files with customizable folders and tags, as well as advanced search capabilities that make it easy to find specific files. Additionally, the server-side compression feature helps reduce the storage requirements for files, freeing up space and increasing efficiency.

In comparison to market leaders in this space, such as Dropbox and Google Drive, the new software offers a more comprehensive file organization and search functionality, as well as an innovative server-side compression feature that significantly reduces storage requirements. Furthermore, the software's scalability allows it to be used by individual users as well as cloud service providers, making it an ideal solution for businesses of all sizes.

The new software offers users a range of features that provide greater flexibility and control over their file management processes. With customizable folders and tags, users can easily organize and access their files, while the advanced search capabilities make it easy to find what they need quickly. The server-side compression feature provides an added layer of efficiency, reducing the storage requirements for files and freeing up valuable space.

Overall, the new remote file management software offers a comprehensive solution for file management that is both scalable and user-friendly. Its advanced file organization and search functionality, combined with server-side compression, make it a competitive player in the market, offering a compelling alternative to current market leaders.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

* [![Flask][Flask.py]][Flask-url]
* [![Tailwind][Tailwind.css]][Tailwind-url]
* [![Python][Python.py]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED 
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
--->
### Installation

1. Go to releases (v1.0) (https://github.com/Dhinuku/Remote-File-Management/releases)
2. Download RFMS.zip and README.md
3. Follow the instructions specified in the README.md and set up the application

Note: Ensure that you have the necessary permissions to access the specified paths and make sure to provide accurate file and directory paths in the configuration files.
If you encounter any issues or have any questions, please contact our support team for assistance.

Thank you for using our application!


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES 
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->


# Features

- [ ] User Management
- [ ] File Management
- [ ] File Organization
- [ ] Searching
- [ ] Sharing
- [ ] File Compression


<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Implementation 
## Architecture
<img src="ARCH DIG.png">
  <br><hr>
Developing a complete remote file management software involves multiple components and
functionalities. Here is a high-level overview of the implementation steps and features that can
be included:

##  User Authentication and Authorization
Implementing user registration and login functionality

### User Registration
1. Create a registration form where users can input their credentials, username and password.
2. On form submission, validate and securely store the user’s credentials in a database.

### User Login
1. Create a login form where users can enter their credentials.
2. On form submission, validate the provided credentials against the stored values in the
database and If the credentials are valid, generate a new unique token for the user.
3. Store the token as a cookie in the user’s browser, setting an expiration time if desired and
associate the token with the user in the server-side storage

### Access Control
1. For protected resources or pages, check if the user has a valid token in their cookie.
2. On each request, retrieve the token from the user’s cookie and validate it against the serverside storage and if the token is valid and matches the user, grant access to the requested resource.
3. If the token is invalid or expired, redirect the user to the login page.

### Logout
1. Provide a logout functionality where users can terminate their session.
2. On logout, remove the token from the user’s cookie and invalidate it on the server-side.
3. Redirect the user to the login page.

## File Upload and Storage
•Allows users to upload files from their local devices.<br>
•Implementing server-side file storage and organization.

## File Management
• Provide a user interface to browse, view, and manage files and folders allow users to upload and delete files and folders.<br>
• Implemented search functionality to find files based on name and types.


## File Compression
<img src="deflate_process.png">
  <br><hr>
File compression is implemented by using the zlib algorithm, which is a widely used compression algorithm that provides lossless data compression.At its core, zlib uses the DEFLATE
algorithm, which combines LZ77 (a sliding window compression algorithm) and Huffman coding (a variable-length prefix coding algorithm).Steps involved in zlib compression:

### Deflate Compression
1. The data to be compressed is divided into a series of blocks.
2. Within each block, LZ77 compression is applied to find repeated sequences of data. Instead
of storing the complete repeated sequence, LZ77 uses a combination of a backward reference
(offset) and a length to represent the repeated data.
3. The compressed LZ77 data is then passed through Huffman coding, where fixed and dynamic Huffman tables are used to assign shorter codes to frequently occurring symbols and
longer codes to less frequent symbols so it reduces the size of compressed data.

### Compression Ratio and Efficiency
1. The compression ratio achieved by zlib depends on the nature of the input data. Highly
repetitive or redundant data tends to compress better, while already compressed data or random
data may not compress significantly.
2. The efficiency of zlib compression is attributed to the combination of LZ77 and Huffman
coding. LZ77 finds repeated patterns and replaces them with references, and Huffman coding
assigns shorter codes to more frequent symbols, resulting in effective compression.
### Decompression
1. The zlib algorithm also supports decompression of the compressed data.
2. The compressed data is processed in reverse: Huffman decoding is applied to obtain the
compressed LZ77 data, and then LZ77 decompression reconstructs the original data by resolving the backward references.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Dhinoo .  [![LinkedIn][linkedin-shield]][linkedin-url] .  k.u12dhinu@gmail.com

Project Link: [Remote-File-Management](https://github.com/Dhinuku/Remote-File-Management)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## References

* [IEEE](https://ieeexplore.ieee.org/Xplore/home.jsp)
* [Flask documentation](https://flask.palletsprojects.com/en/2.2.x/)
* [Stackoverflow](https://stackoverflow.com/)
* [AWS](https://docs.aws.amazon.com/)
* [Python](https://docs.python.org/3/)
* [Google Drive](https://developers.google.com/drive)
* [DropBox](https://www.dropbox.com/developers/documentation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dhinu-k-u-681666253/
[product-screenshot]: images/screenshot.png
[Flask.py]: https://img.shields.io/badge/Flask-FFFFFF?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Tailwind.css]:https://img.shields.io/badge/tailwind-1E2F97?style=for-the-badge&logo=tailwindcss&logoColor=blue
[Tailwind-url]:https://tailwindcss.com/
[Python.py]:	https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://docs.python.org/3/
