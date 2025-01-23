<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br/>
<h3 align="center">Project Contacts Django</h3>

  <p align="center">
    project_description
    <br/>
    <br />
    <a href="https://github.com/HeitorLouzeiro/test-automatizados-selenium/issues">Report Bug</a>
    ·
    <a href="https://github.com/HeitorLouzeiro/test-automatizados-selenium/issues">Request Feature</a>
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
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#collaborators">Collaborators</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project provides a set of automated tests using Selenium WebDriver to verify the correctness of error messages displayed on the "My Account" section of the practice website http://practice.automationtesting.in/. The tests focus on scenarios involving invalid login attempts and registration failures due to missing or invalid input fields. This project is designed to demonstrate basic UI testing using Python and Selenium.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Selenium][Selenium]][Selenium-url]
* [![unittest][unittest]][unittest-url]
* [![Chrome][Chrome]][Chrome-url]

<p align="right">(<a href="#top">back to top</a>)</p>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage
This project is designed to be run as a suite of tests. The tests automate the following actions:

### 1. Accessing the "My Account" Menu
 Navigates to the "My Account" page on the practice website.

### 2. Testing Login Errors
   * Attempts to log in with invalid credentials.
   * Attempts to log in with a blank username.

### 3. Testing Registration Errors
   * Attempts to register with a blank email.
   * Attempts to register with a blank password.
   * Attempts to register with both blank email and password.

### 4.Terminal messages

<p align="center">
      <img src="src/assets/images/terminal.png" alt="log in testes">
    <br/>
</p>

Each test case verifies that the correct error message is displayed for the respective invalid attempt.
<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* [Python 3.6+](https://www.python.org/)
* [ChromeDriver](https://chromedriver.chromium.org/downloads)
* [pip](https://pip.pypa.io/en/stable/installation/)

<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HeitorLouzeiro/test-selenium-error-messages.git
   ```
2. Access the project folder in terminal/cmd
   ```sh
   cd test-selenium-error-messages
   ```
3. Create a virtualenv with Python.
   ```sh
   python -m venv venv
   ```
4. Activate virtualenv.
    * Ubunto
    ```sh
    source venv/bin/activate
    ```

    * MacOs
    ```sh
    source venv/bin/activate
    ```

    * Windows 
    ```sh
     venv/scripts/activate
    ```

5. Install the dependencies.
    ```sh
     pip install -r requirements.txt
    ```
6. Download the ChromeDriver and add it to your system's PATH or specify its location in the test script.

7. Run the tests.
    ```sh
     python main.py
    ```




<p align="right">(<a href="#top">back to top</a>)</p>






<!-- ROADMAP -->
<!-- ROADMAP -->
## Roadmap

- [x] Implement tests for invalid login scenarios.
- [x] Implement tests for blank username login scenario.
- [x] Implement tests for blank email registration scenario.
- [x] Implement tests for blank password registration scenario.
- [x] Implement tests for blank email and password registration scenario.
- [ ] Add more test cases to cover other scenarios

See the [open issues](https://github.com/HeitorLouzeiro/test-automatizados-selenium/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Improvements`)
3. Commit your Changes (`git commit -m 'Add my new Enhancements'`)
4. Push to the Branch (`git push origin feature/Improvements`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/42551436?s=400&u=608a3a665aa424e0d6d59b01fa634650979b72ad&v=4" width="160px;" alt="Foto do Heitor Louzeiro no GitHub"/><br>
        <sub>
          <b>Heitor Louzeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

<div align='center'>  
  <a href="https://www.instagram.com/heitorlouzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank">
  </a> 
  <a href = "mailto:heitorlouzeirodev@gmail.com">
    <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank">    
  </a>
  <a href="https://www.linkedin.com/in/heitor-louzeiro/" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a> 
</div>

Project Link: [https://github.com/HeitorLouzeiro/test-automatizados-selenium](https://github.com/HeitorLouzeiro/test-automatizados-selenium)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HeitorLouzeiro/test-automatizados-selenium.svg?style=for-the-badge
[contributors-url]: https://github.com/HeitorLouzeiro/test-automatizados-selenium/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HeitorLouzeiro/test-automatizados-selenium.svg?style=for-the-badge
[forks-url]: https://github.com/HeitorLouzeiro/test-automatizados-selenium/network/members
[stars-shield]: https://img.shields.io/github/stars/HeitorLouzeiro/test-automatizados-selenium.svg?style=for-the-badge
[stars-url]: https://github.com/HeitorLouzeiro/test-automatizados-selenium/stargazers
[issues-shield]: https://img.shields.io/github/issues/HeitorLouzeiro/test-automatizados-selenium.svg?style=for-the-badge
[issues-url]: https://github.com/HeitorLouzeiro/test-automatizados-selenium/issues
[license-shield]: https://img.shields.io/github/license/HeitorLouzeiro/test-automatizados-selenium.svg?style=for-the-badge
[license-url]: https://github.com/HeitorLouzeiro/test-automatizados-selenium/blob/master/license
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/heitor-louzeiro

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Selenium]: https://img.shields.io/badge/Selenium-4DB33D?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/

[unittest]: https://img.shields.io/badge/unittest-047D9C?style=for-the-badge&logo=python&logoColor=white
[unittest-url]: https://docs.python.org/3/library/unittest.html

[Chrome]: https://img.shields.io/badge/Chrome-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white
[Chrome-url]: https://www.google.com/chrome/
