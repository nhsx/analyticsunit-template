***When publishing your code you need to make sure:***
  
| You’re clear about who owns the code and how others can use it | |
|:---|:---|
| Does your code have an appropriate licence and copyright notice? | **Mandatory** to include *(see Licensing section below)* |
| Is the README clear and concise? |Best practice to include: [example](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)
| Does the README document intended purpose? Has it been reviewed against MHRA 'software as a medical device' guidance? |**Mandatory** check: [flowchart](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/999908/Software_flow_chart_Ed_1-08b-IVD.pdf)|
| Has semantic versioning been used?|Best practice to use *(see versioning section above)*|
| Who has responsibility for ongoing support and communications for the code?|Best practice to assign|
| Have [contribution guidelines](https://github.com/alphagov/govuk-frontend/blob/master/CONTRIBUTING.md) or [PR style guides](https://github.com/alphagov/styleguides/blob/master/pull-requests.md) been included? |Best practice to include|
| Who will address identified issues and security concerns? |**Mandatory** check|
| Has a responsible disclosure process for security issues been defined? |**Mandatory** check|
|||
| **You do not release information that should remain closed** | |
| Does the code include any sensitive, personal, secret or top secret data/information? | **Mandatory** check *(if any identified then see section on dealing with sensitive data in code below)* <br />:white_large_square: No sensitive data <br />:white_large_square: Sensitive <br />:white_large_square: Personal <br />:white_large_square: Secret <br />:white_large_square: Top secret | 
| Does the code include any unreleased policy?| **Mandatory** check *(if any identified then see section on dealing with sensitive data in code below)*|
| Does the code include business sensitive algorithms (e.g. fraud detection)? | **Mandatory** check *(if any identified then see section on dealing with sensitive data in code below)* |
| Has written permission been obtained for any data stored from the data owner? | **Mandatory** to obtain | 
| Are any data transfers conducted safely and securely? (see third-party tools point below) | **Mandatory** check | 
| Are any credentials contained in the source code? | **Mandatory** check in both current version and git history *(see git history guidance if so)* |
| Are any secret keys contained in the source code? | **Mandatory** check in both current version and git history *(see git history guidance if so)* | 
| Are the commit messages informative? | Best practice. If not consider additional documentation to highlight major commit messages | 
| Do the commit messages include any sensitive information (e.g. names)? | **Mandatory** check *(see git history guidance if so)* |
| Does the git history contain any sensitive information (e.g. at one time real data or credentials were in the code but have since been removed) | **Mandatory** check *(see git history guidance if so)* |
| Have notebook outputs been removed/checked for sensitive information? | **Mandatory** check but some appropriate outputs maybe useful: [Example]( https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.pre-commit-config.yaml) |
|||
|**You store it in a repository managed by your department**||
|Is the code stored in your organisational GitHub account? Is it the same organisation that funds the relevant staff time? | Best practice to ensure | 
|||
|**Any third-party tools you use to host or manage your code follow the National Cyber Security Centre’s cloud security guidance**||
| Are third party tools used within the code? | **Mandatory** check. Best practice is to keep an inventory |
| If so do they adhere to the NCSC's [Cloud Security Principles](https://www.ncsc.gov.uk/collection/cloud-security/implementing-the-cloud-security-principles)?| **Mandatory** check |
|||
| **An internal code review has been completed** ||
| Has a colleague reviewed the code for sensitive data content and security vulnerabilities? |**Mandatory** action. Includes third party components. Best practice is to record automated code quality and security tools used |  
