def main():
    import os
    issue_id = os.environ['ISSUE_ID']
    issue_title = os.environ['ISSUE_TITLE']
    issue_body = os.environ['ISSUE_BODY']
    issue_created_at = os.environ['ISSUE_CREATED_AT']
    issue_updated_at = os.environ['ISSUE_UPDATED_AT']

    print (f"issue_id: {issue_id}")
    print (f"issue_title: {issue_title}")
    print (f"issue_body: {issue_body}")
    print (f"issue_created_at: {issue_created_at}")
    print (f"issue_updated_at: {issue_updated_at}")

if __name__ == "__main__":
    main()
