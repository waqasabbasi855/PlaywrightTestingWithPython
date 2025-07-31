class MuseumData:
    def __init__(self, title: str, location: str, phone: str, address: str):
        self.title = title
        self.location = location
        self.phone = phone
        self.address = address

    def __repr__(self):
        return (
            f"MuseumData(title='{self.title}', "
            f"location='{self.location}', "
            f"phone='{self.phone}', "
            f"address='{self.address}')"
        )
