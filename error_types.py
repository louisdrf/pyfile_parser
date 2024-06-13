class FileTypeError(Exception):
    """Exception levée pour une erreur de type de fichier invalide."""
    pass

class NoExtensionError(FileTypeError):
    """Exception levée lorsque le fichier n'a pas d'extension."""
    pass

class UnsupportedFileTypeError(FileTypeError):
    """Exception levée lorsque le type de fichier n'est pas pris en charge."""
    pass