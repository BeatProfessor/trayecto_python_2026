def formato_peso(bytes_):
    """Convierte bytes a texto legible: elige KB, MB, GB o TB según el tamaño."""
    if bytes_ < 1024:
        return f"{round(bytes_,2):,} bytes"
    elif 1024 <= bytes_ < 1024**2:
        return f"{bytes_ / 1024:,.2f} KB"
    elif 1024 ** 2 <= bytes_ < 1024**3:
        return f"{bytes_ / 1024**2:,.2f} MB"
    elif 1024 ** 3 <= bytes_ < 1024**4:
        return f"{bytes_ / 1024**3:,.2f} GB"
    elif bytes_ == 0:
        return "0 bytes"
    else:
        return f"{bytes_ / 1024**4:,.2f} TB"