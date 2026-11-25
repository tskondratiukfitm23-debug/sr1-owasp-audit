# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 1 |
| Medium | 4 |
| Low | 4 |
| Informational | 3 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP errors logged - see the zap.log file for details | 1    |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 8    |
| Info | Informational | http://localhost:3000 | Percentage of responses with status code 1xx | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of responses with status code 2xx | 70 % |
| Info | Informational | http://localhost:3000 | Percentage of responses with status code 3xx | 27 % |
| Info | Informational | http://localhost:3000 | Percentage of responses with status code 4xx | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type application/javascript | 3 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type application/json | 7 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type application/octet-stream | 2 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type image/avif | 9 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type image/jpeg | 7 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type image/png | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type image/svg+xml | 21 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type image/x-icon | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type text/css | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type text/html | 39 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type text/markdown | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with content type text/plain | 1 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with method GET | 97 % |
| Info | Informational | http://localhost:3000 | Percentage of endpoints with method POST | 2 % |
| Info | Informational | http://localhost:3000 | Count of total endpoints | 201    |
| Info | Informational | http://localhost:3000 | Percentage of slow responses | 16 % |
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




## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Off-site Redirect | High | 1 |
| Content Security Policy (CSP) Header Not Set | Medium | Systemic |
| Cross-Domain Misconfiguration | Medium | Systemic |
| Missing Anti-clickjacking Header | Medium | 1 |
| Session ID in URL Rewrite | Medium | Systemic |
| Application Error Disclosure | Low | 2 |
| Private IP Disclosure | Low | 1 |
| Timestamp Disclosure - Unix | Low | 4 |
| X-Content-Type-Options Header Missing | Low | 3 |
| Information Disclosure - Sensitive Information in URL | Informational | 1 |
| Information Disclosure - Suspicious Comments | Informational | 3 |
| Modern Web Application | Informational | Systemic |




## Alert Detail



### [ Off-site Redirect ](https://www.zaproxy.org/docs/alerts/10028/)



##### High (Medium)

### Description

Open redirects are one of the OWASP 2010 Top Ten vulnerabilities. This check looks at user-supplied input in query string parameters and POST data to identify where open redirects might be possible. Open redirects occur when an application allows user-supplied input (e.g. https://nottrusted.com) to control an off-site destination. This is generally a pretty accurate way to find where 301 or 302 redirects could be exploited by spammers or phishing attacks.

For example an attacker could supply a user with the following link: https://example.com/example.php?url=https://malicious.example.com.

NOTE: For the purposes of the passive check the authority portion of the origin and destination were compared. Manual testing may be required to validate the impact of this finding.

* URL: http://localhost:3000/redirect%3Fto=https://github.com/juice-shop/juice-shop
  * Node Name: `http://localhost:3000/redirect (to)`
  * Method: `GET`
  * Parameter: `to`
  * Attack: ``
  * Evidence: ``
  * Other Info: `The 301 or 302 response to a request for the following URL appeared to contain user input in the location header:

http://localhost:3000/redirect?to=https://github.com/juice-shop/juice-shop

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

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://localhost:3000
  * Node Name: `http://localhost:3000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:3000/
  * Node Name: `http://localhost:3000/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:3000/ftp/coupons_2013.md.bak
  * Node Name: `http://localhost:3000/ftp/coupons_2013.md.bak`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:3000/ftp/eastere.gg
  * Node Name: `http://localhost:3000/ftp/eastere.gg`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:3000/sitemap.xml
  * Node Name: `http://localhost:3000/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Cross-Domain Misconfiguration ](https://www.zaproxy.org/docs/alerts/10098/)



##### Medium (Medium)

### Description

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

* URL: http://localhost:3000
  * Node Name: `http://localhost:3000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: http://localhost:3000/assets/public/favicon_js.ico
  * Node Name: `http://localhost:3000/assets/public/favicon_js.ico`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: http://localhost:3000/chunk-3CyVWL1v.js
  * Node Name: `http://localhost:3000/chunk-3CyVWL1v.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`
* URL: http://localhost:3000/styles.css
  * Node Name: `http://localhost:3000/styles.css`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Access-Control-Allow-Origin: *`
  * Other Info: `The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.`

Instances: Systemic


### Solution

Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).
Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

### Reference


* [ https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy ](https://vulncat.fortify.com/en/detail?category=HTML5&subcategory=Overly%20Permissive%20CORS%20Policy)


#### CWE Id: [ 264 ](https://cwe.mitre.org/data/definitions/264.html)


#### WASC Id: 14

#### Source ID: 3

### [ Missing Anti-clickjacking Header ](https://www.zaproxy.org/docs/alerts/10020/)



##### Medium (Medium)

### Description

The response does not protect against 'ClickJacking' attacks. It should include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options.

* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95jbonz&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.
If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options)


#### CWE Id: [ 1021 ](https://cwe.mitre.org/data/definitions/1021.html)


#### WASC Id: 15

#### Source ID: 3

### [ Session ID in URL Rewrite ](https://www.zaproxy.org/docs/alerts/3/)



##### Medium (High)

### Description

URL rewrite is used to track user session ID. The session ID may be disclosed via cross-site referer header. In addition, the session ID might be stored in browser history or server logs.

* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95jcv8c&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)`
  * Method: `GET`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `gc84oHKD07pzXIETAAB7`
  * Other Info: ``
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o981jsaq&sid=lfLGs1tj2OxSpfy7AAB8
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)`
  * Method: `GET`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `lfLGs1tj2OxSpfy7AAB8`
  * Other Info: ``
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=websocket&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,transport)`
  * Method: `GET`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `gc84oHKD07pzXIETAAB7`
  * Other Info: ``
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95jbonz&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `gc84oHKD07pzXIETAAB7`
  * Other Info: ``
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o981ifwb&sid=lfLGs1tj2OxSpfy7AAB8
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `sid`
  * Attack: ``
  * Evidence: `lfLGs1tj2OxSpfy7AAB8`
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

* URL: http://localhost:3000/api/Feedbacks/
  * Node Name: `http://localhost:3000/api/Feedbacks/ ()({captcha,comment,rating})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: http://localhost:3000/rest/user/reset-password
  * Node Name: `http://localhost:3000/rest/user/reset-password ()({email,answer,new,repeat})`
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

* URL: http://localhost:3000/rest/admin/application-configuration
  * Node Name: `http://localhost:3000/rest/admin/application-configuration`
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

* URL: http://localhost:3000/rest/admin/application-configuration
  * Node Name: `http://localhost:3000/rest/admin/application-configuration`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1969196030`
  * Other Info: `1969196030, which evaluates to: 2032-05-26 14:53:50.`
* URL: http://localhost:3000/rest/admin/application-configuration
  * Node Name: `http://localhost:3000/rest/admin/application-configuration`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1970691216`
  * Other Info: `1970691216, which evaluates to: 2032-06-12 22:13:36.`
* URL: http://localhost:3000/rest/products/search%3Fq=
  * Node Name: `http://localhost:3000/rest/products/search (q)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `1969196030`
  * Other Info: `1969196030, which evaluates to: 2032-05-26 14:53:50.`
* URL: http://localhost:3000/rest/products/search%3Fq=
  * Node Name: `http://localhost:3000/rest/products/search (q)`
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

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95jcv8c&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95gk34e
  * Node Name: `http://localhost:3000/socket.io/ (EIO,t,transport)`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:3000/socket.io/%3FEIO=4&transport=polling&t=o95jbonz&sid=gc84oHKD07pzXIETAAB7
  * Node Name: `http://localhost:3000/socket.io/ (EIO,sid,t,transport)(40)`
  * Method: `POST`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 3

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Information Disclosure - Sensitive Information in URL ](https://www.zaproxy.org/docs/alerts/10024/)



##### Informational (Medium)

### Description

The request appeared to contain sensitive information leaked in the URL. This can violate PCI and most organizational compliance policies. You can configure the list of strings for this check to add or remove values specific to your environment.

* URL: http://localhost:3000/rest/user/security-question%3Femail=foo-bar@example.com
  * Node Name: `http://localhost:3000/rest/user/security-question (email)`
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

* URL: http://localhost:3000/chunk-3CyVWL1v.js
  * Node Name: `http://localhost:3000/chunk-3CyVWL1v.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `select`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//`)).test(e)){let[,t]=e.split(/\/\/[^\/]+/);return t}return e}function vv(e){return Oe(e)[le.LocaleId]}function Dv(e,n,t){let r", see evidence field for the suspicious comment/snippet.`
* URL: http://localhost:3000/chunk-CajNVifV.js
  * Node Name: `http://localhost:3000/chunk-CajNVifV.js`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `SELECT`
  * Other Info: `The following pattern was used: \bSELECT\b and was detected in likely comment: "//`)}catch(t){return!0}}function Fn(n){return n.segments.map(t=>Rs(t)).join(`/`)}function ut(n,t){if(!n.hasChildren())return Fn(", see evidence field for the suspicious comment/snippet.`
* URL: http://localhost:3000/main.js
  * Node Name: `http://localhost:3000/main.js`
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

* URL: http://localhost:3000
  * Node Name: `http://localhost:3000`
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
* URL: http://localhost:3000/
  * Node Name: `http://localhost:3000/`
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
* URL: http://localhost:3000/home/ubuntu/sr1/tools_dl/juice-shop_20.4.0-SNAPSHOT/build/routes/fileServer.js:68:18
  * Node Name: `http://localhost:3000/home/ubuntu/sr1/tools_dl/juice-shop_20.4.0-SNAPSHOT/build/routes/fileServer.js:68:18`
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
* URL: http://localhost:3000/home/ubuntu/sr1/tools_dl/juice-shop_20.4.0-SNAPSHOT/node_modules/express/lib/router/index.js:328:13
  * Node Name: `http://localhost:3000/home/ubuntu/sr1/tools_dl/juice-shop_20.4.0-SNAPSHOT/node_modules/express/lib/router/index.js:328:13`
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
* URL: http://localhost:3000/sitemap.xml
  * Node Name: `http://localhost:3000/sitemap.xml`
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

Instances: Systemic


### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3


