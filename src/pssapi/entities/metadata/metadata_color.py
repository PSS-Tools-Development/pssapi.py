class Color(object):
    def __init__(self, color_string: str):
        self._a: float = 255

        self._r: int = 0
        self._g: int = 0
        self._b: int = 0

        if color_string:
            if color_string.startswith("#"):
                if len(color_string) == 7:
                    self._r = int(color_string[1:3], 16)
                    self._g = int(color_string[3:5], 16)
                    self._b = int(color_string[5:7], 16)
                else:
                    raise ValueError(f"The parameter color received an unsupported value: {color_string}")
            elif "," in color_string:
                colors = [int(color.strip()) for color in color_string.split(",")]
                if len(colors) == 3:
                    self._r, self._g, self._b = colors
                else:
                    raise ValueError(f"The parameter color received an unsupported value: {color_string}")
            else:
                raise ValueError(f"The parameter color received an unsupported value: {color_string}")

    @property
    def alpha(self) -> int:
        return self._a

    @property
    def blue(self) -> int:
        return self._b

    @property
    def green(self) -> int:
        return self._g

    @property
    def red(self) -> int:
        return self._r

    def get_hex_string(self) -> str:
        return f"#{self.red:x}{self.green:x}{self.blue:x}"

    def get_rgb_string(self) -> str:
        return ",".join((self.red, self.green, self.blue))
