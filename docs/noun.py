get_all_nouns_responses = {
    200: {
        "description": "Return a pageable collection of available Nouns in the database.",
        "content": {
            "application/json": {
                "example": {
                    "items": [
                        {
                            "noun": "Apfel",
                            "articles": {
                                "nominative": "der",
                                "accusative": "den",
                                "dative": "den",
                                "genitive": "der"
                            }
                        },
                        {
                            "noun": "Angst",
                            "articles": {
                                "nominative": "die",
                                "accusative": "die",
                                "dative": "dem",
                                "genitive": "des"
                            }
                        }
                    ],
                    "total": 2,
                    "page": 1,
                    "size": 50
                }
            }
        },
    },
    422: {
        "description": "Some of the query params is invalid. Probably, it is 'gender', which can be only:"
                       " masculine, feminine or neutral.",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": [
                                "query",
                                "gender"
                            ],
                            "msg": "value is not a valid enumeration member; permitted:"
                                   " 'masculine', 'feminine', 'neutral'",
                            "type": "type_error.enum",
                            "ctx": {
                                "enum_values": [
                                    "masculine",
                                    "feminine",
                                    "neutral"
                                ]
                            }
                        }
                    ]
                }
            }
        },
    }
}

get_noun_responses = {
    200: {
        "description": "Return the searched Noun informations.",
        "content": {
            "application/json": {
                "example": {
                    "noun": "Apfel",
                    "articles": {
                        "nominative": "der",
                        "accusative": "den",
                        "dative": "den",
                        "genitive": "der"
                    }
                }
            }
        }
    },
    404: {
        "description": "The searched Noun does not exist in the database.",
        "content": {
            "application/json": {
                "example": {
                    "detail": {
                        "message": "Noun 'Hund' was not found",
                        "procedure": "If you are sure that it sould exist, please contact me at "
                                     "andrew.agoravai@gmail.com",
                        "url": "/api/v1/nouns/Hund"
                    }
                }
            }
        }
    },
    422: {
        "description": "This is shown by FastAPI by default, but it does not occur in this case =)."
    }
}
