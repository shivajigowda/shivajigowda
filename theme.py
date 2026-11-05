"""Light and dark palettes. Paper, ink and accents follow the deck's visual language:
off-white paper, near-black ink, electric purple for key words, pastel chips, rare warm accents.
Every *_ink token keeps >= 4.5:1 contrast on its own fill."""

LIGHT = dict(
    name="light",
    paper="#F7F6F1", card="#FFFFFF", card_line="#E6E4DC", shadow="#151515",
    ink="#151515", ink2="#3C3C3C", muted="#6B6B6B", faint="#9A9A9A", line="#DCDAD1",
    purple="#6E22FE", purple_fill="#6E22FE", lav="#CBB7F9", lav_soft="#F2ECFE", lav_ink="#3A1F86",
    lime="#E9FD70", grn="#C2FE80", grn_soft="#EDFEDC", grn_ink="#0F4C00", grn2="#3F8F0A",
    yellow="#FDF049", yellow_soft="#FEFBD6", yellow_ink="#5C5200",
    orange="#D8731C", gold="#C9A800", crimson="#D81B4D",
    glow_a="#C2FE80", glow_b="#CBB7F9", glow_op=0.55, warm_a="#FFD9A8", warm_b="#F9C6D6", band="#FFFFFF", band_op=0.55,
    ms_fill="#151515", ms_text="#FDF049", ms_ring="#FFFFFF",
    core_fill="#151515", core_text="#FFFFFF",
    bubbles=dict(
        lime=("#E9FD70", "#2B3A00"), lilac=("#E9DCFB", "#3A1F86"), yellow=("#FEF3A0", "#4F4600"),
        peach=("#FBDCC8", "#7A3410"), sky=("#D6ECF8", "#0B4A6E"), pink=("#F9D6E3", "#7A1037"),
        mint=("#CDF3DC", "#0F5A2F"), violet=("#7A3CFF", "#FFFFFF")),
)

DARK = dict(
    name="dark",
    paper="#0F0D1A", card="#1A1729", card_line="#2E2A42", shadow="#000000",
    ink="#F4F2FB", ink2="#D3CFE2", muted="#A7A2BB", faint="#7D7893", line="#353049",
    purple="#B197FF", purple_fill="#7A3CFF", lav="#5B47A8", lav_soft="#231C3F", lav_ink="#DCCFFF",
    lime="#E9FD70", grn="#9BE35A", grn_soft="#18260F", grn_ink="#C2FE80", grn2="#8BD24A",
    yellow="#FDF049", yellow_soft="#2C2812", yellow_ink="#FDF049",
    orange="#F0954A", gold="#E6C93A", crimson="#FF5C86",
    glow_a="#6E9E1E", glow_b="#6B3FE0", glow_op=0.7, warm_a="#9A4A14", warm_b="#8A1E44", band="#FFFFFF", band_op=0.025,
    ms_fill="#FDF049", ms_text="#151515", ms_ring="#0F0D1A",
    core_fill="#F4F2FB", core_text="#151515",
    bubbles=dict(
        lime=("#2F3A10", "#E9FD70"), lilac=("#2C2250", "#DCCFFF"), yellow=("#38320F", "#FDF049"),
        peach=("#3D2416", "#FFC29A"), sky=("#132F3F", "#9ED8F5"), pink=("#3D1626", "#FFA8C6"),
        mint=("#123222", "#9EEDBE"), violet=("#7A3CFF", "#FFFFFF")),
)

THEMES = {"light": LIGHT, "dark": DARK}
