"""Desenhos vetoriais; a altura preenchida representa uma fração de 0 a 1."""

from math import isfinite


def _fracao(valor):
    numero = 0.0 if valor is None else float(valor)
    return max(0.0, min(1.0, numero)) if isfinite(numero) else 0.0


def gol_svg(preenchimento=0):
    altura = 170 * _fracao(preenchimento)
    rede_vertical = "".join(
        f'<path d="M{x} 35 V205"/>' for x in range(85, 566, 48)
    )
    rede_horizontal = "".join(
        f'<path d="M35 {y} H615"/>' for y in range(69, 205, 34)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 245">
      <rect width="650" height="245" rx="18" fill="#f8fafc"/>
      <rect x="35" y="{205-altura}" width="580" height="{altura}" fill="#86efac"/>
      <g fill="none" stroke="#cbd5e1" stroke-width="2">
        {rede_vertical}{rede_horizontal}
      </g>
      <path d="M35 205 V35 H615 V205" fill="none" stroke="#166534"
        stroke-width="9" stroke-linejoin="round"/>
      <path d="M20 210 H630" stroke="#166534" stroke-width="3"/>
    </svg>'''


def chuteira_svg(preenchimento=0):
    altura = 84 * _fracao(preenchimento)
    formato = "M26 104 V60 L52 32 L76 56 L100 52 L114 80 L158 88 L184 96 Q216 99 216 116 L25 116 Z"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150">
      <rect width="240" height="150" rx="14" fill="#f8fafc"/>
      <defs><clipPath id="chuteira"><path d="{formato}"/></clipPath></defs>
      <rect x="25" y="{116-altura}" width="195" height="{altura}" fill="#4ade80" clip-path="url(#chuteira)"/>
      <path d="{formato}"
        fill="none" stroke="#166534" stroke-width="5" stroke-linejoin="round"/>
      <g stroke="#166534" stroke-width="4" fill="none">
        <path d="M84 65 L109 60 M91 75 L116 70 M99 85 L125 79"/>
        <path d="M41 118 V128 M78 118 V128 M162 118 V128 M197 118 V128"/>
      </g>
    </svg>'''


def cartao_svg(cor, preenchimento=0):
    altura = 120 * _fracao(preenchimento)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150">
      <rect width="240" height="150" rx="14" fill="#f8fafc"/>
      <defs><clipPath id="cartao"><rect x="77" y="15" width="86" height="120" rx="9"/></clipPath></defs>
      <rect x="77" y="{135-altura}" width="86" height="{altura}" fill="{cor}" opacity="0.75" clip-path="url(#cartao)"/>
      <rect x="77" y="15" width="86" height="120" rx="9"
        fill="none" stroke="{cor}" stroke-width="6"/>
    </svg>'''
