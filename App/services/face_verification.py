from deepface import DeepFace


def verify_faces(selfie_path, id_card_path):

    try:

        result = DeepFace.verify(
            img1_path=selfie_path,
            img2_path=id_card_path,
            enforce_detection=False
        )

        return {
            "verified": result["verified"],
            "distance": result["distance"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }