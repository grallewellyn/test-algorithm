from maap.maap import MAAP
print("graceal1 before instantiating maap")
maap = MAAP()

print("graceal1 before adding secrets")
maap.secrets.add_secret("MY_TOKEN", "98aj48j(774hh9*H")

print("graceal1 before printing secrets")
print(maap.secrets.get_secrets())

print("graceal1 before deleting secrets")
maap.secrets.delete_secret("MY_TOKEN")

print("graceal1 before printing secrets last time")
print(maap.secrets.get_secrets())