helps = """
Run GPWD.

Checks for existence of username on various social media sites.

Keyword Arguments:
username               -- String indicating username that report
                        should be created against.
site_data              -- Dictionary containing all of the site data.
query_notify           -- Object with base type of QueryNotify().
                        This will be used to notify the caller about
                        query results.
tor                    -- Boolean indicating whether to use a tor circuit for the requests.
unique_tor             -- Boolean indicating whether to use a new tor circuit for each request.
proxy                  -- String indicating the proxy URL
timeout                -- Time in seconds to wait before timing out request.
                        Default is 60 seconds.

Return Value:
Dictionary containing results from report. Key of dictionary is the name
of the social network site, and the value is another dictionary with
the following keys:
    url_main:      URL of main site.
    url_user:      URL of user on site (if account exists).
    status:        QueryResult() object indicating results of test for
                account existence.
    http_status:   HTTP status code of query which checked for existence on
                site.
    response_text: Text that came back from request.  May be None if
                there was an HTTP error when checking for existence.
"""

def Helps_menu(helps=helps):
    print(helps)