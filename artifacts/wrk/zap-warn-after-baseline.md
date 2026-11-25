# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 1 |
| Medium | 2 |
| Low | 3 |
| Informational | 4 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP errors logged - see the zap.log file for details | 1    |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 9    |
| Info | Informational | https://content-signature-2.cdn.mozilla.net | Percentage of endpoints with content type text/plain | 100 % |
| Info | Informational | https://content-signature-2.cdn.mozilla.net | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://content-signature-2.cdn.mozilla.net | Count of total endpoints | 2    |
| Info | Informational | https://firefox-settings-attachments.cdn.mozilla.net | Percentage of endpoints with content type application/octet-stream | 3 % |
| Info | Informational | https://firefox-settings-attachments.cdn.mozilla.net | Percentage of endpoints with content type application/x-protobuf | 80 % |
| Info | Informational | https://firefox-settings-attachments.cdn.mozilla.net | Percentage of endpoints with content type text/plain | 16 % |
| Info | Informational | https://firefox-settings-attachments.cdn.mozilla.net | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://firefox-settings-attachments.cdn.mozilla.net | Count of total endpoints | 98    |
| Info | Informational | https://firefox.settings.services.mozilla.com | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://firefox.settings.services.mozilla.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://firefox.settings.services.mozilla.com | Count of total endpoints | 39    |
| Info | Informational | https://github.com | Percentage of endpoints with content type text/html | 100 % |
| Info | Informational | https://github.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://github.com | Count of total endpoints | 1    |
| Info | Informational | https://localhost:8443 | Percentage of responses with status code 1xx | 1 % |
| Info | Informational | https://localhost:8443 | Percentage of responses with status code 2xx | 74 % |
| Info | Informational | https://localhost:8443 | Percentage of responses with status code 3xx | 22 % |
| Info | Informational | https://localhost:8443 | Percentage of responses with status code 4xx | 4 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type application/javascript | 7 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type application/json | 16 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type font/woff2 | 1 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type image/avif | 13 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type image/jpeg | 13 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type image/png | 2 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type image/svg+xml | 35 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type image/x-icon | 1 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type text/css | 1 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type text/html | 6 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with content type text/plain | 2 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with method GET | 94 % |
| Info | Informational | https://localhost:8443 | Percentage of endpoints with method POST | 5 % |
| Info | Informational | https://localhost:8443 | Count of total endpoints | 123    |
| Info | Informational | https://localhost:8443 | Percentage of slow responses | 17 % |




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Off-site Redirect | High | 1 |
| CSP: style-src unsafe-inline | Medium | Systemic |
| Session ID in URL Rewrite | Medium | Systemic |
| Application Error Disclosure | Low | 2 |
| Private IP Disclosure | Low | 1 |
| Timestamp Disclosure - Unix | Low | 4 |
| Information Disclosure - Sensitive Information in URL | Informational | 1 |
| Information Disclosure - Suspicious Comments | Informational | 3 |
| Modern Web Application | Informational | 4 |
| Re-examine Cache-control Directives | Informational | Systemic |




## Alert Detail



### [ Off-site Redirect ](https://www.zaproxy.org/docs/alerts/10028/)



##### High (Medium)

### Description

Open redirects are one of the OWASP 2010 Top Ten vulnerabilities. This check looks at user-supplied input in query string parameters and POST data to identify where open redirects might be possible. Open redirects occur when an application allows user-supplied input (e.g. https://nottrusted.com) to control an off-site destination. This is generally a pretty accurate way to find where 301 or 302 redirects could be exploited by spammers or phishing attacks.

For example an attacker could supply a user with the following link: https://example.com/example.php?url=https://malicious.example.com.

NOTE: For the purposes of the passive check the authority portion of the origin and destination were compared. Manual testing may be required to validate the impact of this finding.

* URL: https://localhost:8443/redirect%3Fto=https://github.com/juice-shop/juice-shop
  * Node Name: `https://localhost:8443/redirect (to)`
  * Method: `GET`
  * Parameter: `to`
  * Attack: ``
  * Evidence: ``
  * Other Info: `The 301 or 302 response to a request for the following URL appeared to contain user input in the location header:

https://localhost:8443/redirect?to=https://github.com/juice-shop/juice-shop

The user input found was:

to=https://github.com/juice-shop/juice-shop

The context was:

https://github.com/juice-shop/juice-shop`


Instances: 1

### Solution

To avoid the open redirect vulnerability, parameters of the application script/program must be validated before sending 302 HTTP code (redirect) to the client browser. Implement safe redirect functionality that only redirects to relative URI's, or a list of trusted domains.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/601.html ](https://cwe.mitre.org/data/definitions/601.html)


#### CWE Id: [ 601 ](https://cwe.mitre.org/data/definitions/601.html)


#### WASC Id: 38

#### Source ID: 3

### [ CSP: style-src unsafe-inline ](https://www.zaproxy.org/docs/alerts/10055/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks. Including (but not limited to) Cross Site Scripting (XSS), and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: https://localhost:8443
  * Node Name: `https://localhost:8443`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `default-src 'self'; script-src 'self' 'sha256-2ADpmZIga9zdrCfzZ7IWyavasltpcKCkxomklfMTCG0=' 'sha256-LMY6wYoFV9I4wWzxaq1N/dTpl4iurQktw706UCHK3vM='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' wss://localhost:8443; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://localhost:8443/
  * Node Name: `https://localhost:8443/`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `default-src 'self'; script-src 'self' 'sha256-2ADpmZIga9zdrCfzZ7IWyavasltpcKCkxomklfMTCG0=' 'sha256-LMY6wYoFV9I4wWzxaq1N/dTpl4iurQktw706UCHK3vM='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' wss://localhost:8443; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://localhost:8443/sitemap.xml
  * Node Name: `https://localhost:8443/sitemap.xml`
  * Method: `GET`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `default-src 'self'; script-src 'self' 'sha256-2ADpmZIga9zdrCfzZ7IWyavasltpcKCkxomklfMTCG0=' 'sha256-LMY6wYoFV9I4wWzxaq1N/dTpl4iurQktw706UCHK3vM='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' wss://localhost:8443; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1yaskcs&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `default-src 'self'; script-src 'self' 'sha256-2ADpmZIga9zdrCfzZ7IWyavasltpcKCkxomklfMTCG0=' 'sha256-LMY6wYoFV9I4wWzxaq1N/dTpl4iurQktw706UCHK3vM='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' wss://localhost:8443; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'`
  * Other Info: `style-src includes unsafe-inline.`
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1ybkm60&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)(42["notification received","ff4aebffe31b...)`
  * Method: `POST`
  * Parameter: `Content-Security-Policy`
  * Attack: ``
  * Evidence: `default-src 'self'; script-src 'self' 'sha256-2ADpmZIga9zdrCfzZ7IWyavasltpcKCkxomklfMTCG0=' 'sha256-LMY6wYoFV9I4wWzxaq1N/dTpl4iurQktw706UCHK3vM='; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self' wss://localhost:8443; frame-src 'none'; frame-ancestors 'none'; object-src 'none'; base-uri 'self'; form-action 'self'`
  * Other Info: `style-src includes unsafe-inline.`

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is properly configured to set the Content-Security-Policy header.

### Reference


* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://caniuse.com/#search=content+security+policy ](https://caniuse.com/#search=content+security+policy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)
* [ https://github.com/HtmlUnit/htmlunit-csp ](https://github.com/HtmlUnit/htmlunit-csp)
* [ https://web.dev/articles/csp#resource-options ](https://web.dev/articles/csp#resource-options)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Session ID in URL Rewrite ](https://www.zaproxy.org/docs/alerts/3/)



##### Medium (High)

### Description

URL rewrite is used to track user session ID. The session ID may be disclosed via cross-site referer header. In addition, the session ID might be stored in browser history or server logs.

* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1yat08h&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)`
  * Method: `GET`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `sl74-V1qCU5xzXZ0AAAA`
  * Other Info: ``
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=websocket&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,transport)`
  * Method: `GET`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `sl74-V1qCU5xzXZ0AAAA`
  * Other Info: ``
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1yaskcs&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `sl74-V1qCU5xzXZ0AAAA`
  * Other Info: ``
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1ycwltr&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)(42["notification received","690fa3247a99...)`
  * Method: `POST`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `sl74-V1qCU5xzXZ0AAAA`
  * Other Info: ``
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1ybkm60&sid=sl74-V1qCU5xzXZ0AAAA
  * Node Name: `https://localhost:8443/socket.io/ (EIO,sid,t,transport)(42["notification received","ff4aebffe31b...)`
  * Method: `POST`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `sl74-V1qCU5xzXZ0AAAA`
  * Other Info: ``

Instances: Systemic


### Solution

For secure content, put session ID in a cookie. To be even more secure consider using a combination of cookie and URL rewrite.

### Reference


* [ https://seclists.org/webappsec/2002/q4/111 ](https://seclists.org/webappsec/2002/q4/111)


#### CWE Id: [ 598 ](https://cwe.mitre.org/data/definitions/598.html)


#### WASC Id: 13

#### Source ID: 3

### [ Application Error Disclosure ](https://www.zaproxy.org/docs/alerts/90022/)



##### Low (Medium)

### Description

This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.

* URL: https://localhost:8443/api/Feedbacks/
  * Node Name: `https://localhost:8443/api/Feedbacks/ ()({captcha,comment,rating})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: https://localhost:8443/rest/user/reset-password
  * Node Name: `https://localhost:8443/rest/user/reset-password ()({email,answer,new,repeat})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``


Instances: 2

### Solution

Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

### Reference



#### CWE Id: [ 550 ](https://cwe.mitre.org/data/definitions/550.html)


#### WASC Id: 13

#### Source ID: 3

### [ Private IP Disclosure ](https://www.zaproxy.org/docs/alerts/2/)



##### Low (Medium)

### Description

A private IP (such as 10.x.x.x, 172.x.x.x, 192.168.x.x) or an Amazon EC2 private hostname (for example, ip-10-0-56-78) has been found in the HTTP response body. This information might be helpful for further attacks targeting internal systems.

* URL: https://localhost:8443/rest/admin/application-configuration
  * Node Name: `https://localhost:8443/rest/admin/application-configuration`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `192.168.99.100:3000`
  * Other Info: `192.168.99.100:3000
192.168.99.100:4200
`


Instances: 1

### Solution

Remove the private IP address from the HTTP response body. For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc1918 ](https://datatracker.ietf.org/doc/html/rfc1918)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Timestamp Disclosure - Unix ](https://www.zaproxy.org/docs/alerts/10096/)



##### Low (Low)

### Description

A timestamp was disclosed by the application/web server. - Unix

* URL: https://localhost:8443/rest/admin/application-configuration
  * Node Name: `https://localhost:8443/rest/admin/application-configuration`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1969196030`
  * Other Info: `1969196030, which evaluates to: 2032-05-26 14:53:50.`
* URL: https://localhost:8443/rest/admin/application-configuration
  * Node Name: `https://localhost:8443/rest/admin/application-configuration`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1970691216`
  * Other Info: `1970691216, which evaluates to: 2032-06-12 22:13:36.`
* URL: https://localhost:8443/rest/products/search%3Fq=
  * Node Name: `https://localhost:8443/rest/products/search (q)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1969196030`
  * Other Info: `1969196030, which evaluates to: 2032-05-26 14:53:50.`
* URL: https://localhost:8443/rest/products/search%3Fq=
  * Node Name: `https://localhost:8443/rest/products/search (q)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1970691216`
  * Other Info: `1970691216, which evaluates to: 2032-06-12 22:13:36.`


Instances: 4

### Solution

Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

### Reference


* [ https://cwe.mitre.org/data/definitions/200.html ](https://cwe.mitre.org/data/definitions/200.html)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Information Disclosure - Sensitive Information in URL ](https://www.zaproxy.org/docs/alerts/10024/)



##### Informational (Medium)

### Description

The request appeared to contain sensitive information leaked in the URL. This can violate PCI and most organizational compliance policies. You can configure the list of strings for this check to add or remove values specific to your environment.

* URL: https://localhost:8443/rest/user/security-question%3Femail=foo-bar@example.com
  * Node Name: `https://localhost:8443/rest/user/security-question (email)`
  * Method: `GET`
  * Parameter: `email`
  * Attack: ``
  * Evidence: `foo-bar@example.com`
  * Other Info: `The URL contains email address(es).`


Instances: 1

### Solution

Do not pass sensitive information in URIs.

### Reference



#### CWE Id: [ 598 ](https://cwe.mitre.org/data/definitions/598.html)


#### WASC Id: 13

#### Source ID: 3

### [ Information Disclosure - Suspicious Comments ](https://www.zaproxy.org/docs/alerts/10027/)



##### Informational (Low)

### Description

The response appears to contain suspicious comments which may help an attacker.

* URL: https://localhost:8443/chunk-3CyVWL1v.js
  * Node Name: `https://localhost:8443/chunk-3CyVWL1v.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `select`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//`)).test(e)){let[,t]=e.split(/\/\/[^\/]+/);return t}return e}function vv(e){return Oe(e)[le.LocaleId]}function Dv(e,n,t){let r", see evidence field for the suspicious comment/snippet.`
* URL: https://localhost:8443/chunk-CajNVifV.js
  * Node Name: `https://localhost:8443/chunk-CajNVifV.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `SELECT`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//`)}catch(t){return!0}}function Fn(n){return n.segments.map(t=>Rs(t)).join(`/`)}function ut(n,t){if(!n.hasChildren())return Fn(", see evidence field for the suspicious comment/snippet.`
* URL: https://localhost:8443/main.js
  * Node Name: `https://localhost:8443/main.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `query`
  * Other Info: `The following pattern was used: \bQUERY\b and was detected in likely comment: "//`+this._hostname()+this._port()+this.opts.path+this._query(t)}_hostname(){let a=this.opts.hostname;return a.indexOf(`:`)===-1?", see evidence field for the suspicious comment/snippet.`


Instances: 3

### Solution

Remove all comments that return information that may help an attacker and fix any underlying problems they refer to.

### Reference



#### CWE Id: [ 615 ](https://cwe.mitre.org/data/definitions/615.html)


#### WASC Id: 13

#### Source ID: 3

### [ Modern Web Application ](https://www.zaproxy.org/docs/alerts/10109/)



##### Informational (Medium)

### Description

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

* URL: https://localhost:8443
  * Node Name: `https://localhost:8443`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://localhost:8443/
  * Node Name: `https://localhost:8443/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://localhost:8443/favicon.ico
  * Node Name: `https://localhost:8443/favicon.ico`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`
* URL: https://localhost:8443/sitemap.xml
  * Node Name: `https://localhost:8443/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`
  * Other Info: `No links have been found while there are scripts, which is an indication that this is a modern web application.`


Instances: 4

### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://localhost:8443
  * Node Name: `https://localhost:8443`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=0`
  * Other Info: ``
* URL: https://localhost:8443/
  * Node Name: `https://localhost:8443/`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=0`
  * Other Info: ``
* URL: https://localhost:8443/robots.txt
  * Node Name: `https://localhost:8443/robots.txt`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://localhost:8443/sitemap.xml
  * Node Name: `https://localhost:8443/sitemap.xml`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `public, max-age=0`
  * Other Info: ``
* URL: https://localhost:8443/socket.io/%3FEIO=4&transport=polling&t=n1y8bwyq
  * Node Name: `https://localhost:8443/socket.io/ (EIO,t,transport)`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``

Instances: Systemic


### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3


