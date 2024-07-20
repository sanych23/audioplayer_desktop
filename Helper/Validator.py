class Validator:
    @staticmethod
    def check_album_data(data: dict):
        if data["name"] and len(data["name"]) > 3:
            data["name"] = data["name"].strip()
        else: 
            return False

        if not data["description"].strip():
            return False
        
        date = data["release_date"].split(".")
        
        if len(date) != 3:
            return False
        
        return True
