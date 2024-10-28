email_distro = {
    "chuck_r@gmail.com": "2023-10-20",
    "big_joe_mcgurk@hotmail.com": "2023-10-18",
    "billy_bob@myemail.net": "2023-10-15"
}

# Access a contact's last interaction date
contact_date = email_distro.get("big_joe_mcgurk@hotmail.com", "Not Found")
print(f"Last contacted on: {contact_date}")
