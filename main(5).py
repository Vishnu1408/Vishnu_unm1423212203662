def list_repositories(username):
  try:
    # Provide your GitHub personal access token here
    g = Github("YOUR_PERSONAL_ACCESS_TOKEN")

    user = g.get_user(username)
    repositories = user.get_repos()

    print(f"Repositories for {username}:")
    for repo in repositories:
      print(repo.name)

  except Exception as e:
    print(f"An error occurred: {e}")
