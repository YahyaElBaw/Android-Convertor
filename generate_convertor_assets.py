import os
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = os.path.abspath(r"D:\L3MDW\Mobile\Convertor\screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def get_converter_phone_html(devise_source="USD", devise_cible="EUR", montant="0", resultat="", toast_msg=None):
    toast_html = f'''
    <div style="position: absolute; bottom: 35px; left: 50%; transform: translateX(-50%); background: #323232; color: white; padding: 10px 18px; border-radius: 20px; font-size: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); z-index: 100; text-align: center; white-space: nowrap;">
        {toast_msg}
    </div>
    ''' if toast_msg else ''

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
            body {{ background: transparent; display: flex; justify-content: center; align-items: center; padding: 20px; }}
            .phone-frame {{
                width: 340px;
                height: 680px;
                background: white;
                border-radius: 36px;
                border: 9px solid #1E293B;
                box-shadow: 0 20px 40px rgba(0,0,0,0.25);
                display: flex;
                flex-direction: column;
                position: relative;
                overflow: hidden;
            }}
            .notch {{
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 120px;
                height: 18px;
                background: #1E293B;
                border-bottom-left-radius: 12px;
                border-bottom-right-radius: 12px;
                z-index: 50;
            }}
            .status-bar {{
                height: 28px;
                background: #2BB8E8;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 16px;
                color: white;
                font-size: 11px;
                font-weight: 600;
            }}
            .zone-haut {{
                height: 310px;
                background: #2BB8E8;
                padding: 12px 18px;
                display: flex;
                flex-direction: column;
                color: white;
                position: relative;
            }}
            .titre-app {{
                text-align: center;
                font-size: 17px;
                font-weight: bold;
                letter-spacing: 0.5px;
                margin-bottom: 8px;
            }}
            .row-devise {{
                display: flex;
                justify-content: space-between;
                align-items: flex-end;
                margin-top: 6px;
            }}
            .spinner-box {{
                background: rgba(255, 255, 255, 0.2);
                border-radius: 6px;
                padding: 4px 10px;
                font-size: 16px;
                font-weight: bold;
                display: inline-flex;
                align-items: center;
                gap: 6px;
            }}
            .montant-display {{
                flex: 1;
                text-align: right;
                font-size: 40px;
                font-weight: 700;
                line-height: 1;
                border-bottom: 2px solid #6ED5F5;
                padding-bottom: 4px;
                margin-left: 14px;
            }}
            .btn-inverser {{
                width: 36px;
                height: 36px;
                margin: 4px 0 4px 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
            }}
            .btn-convertir {{
                background: #88C8F7;
                color: #1565C0;
                font-size: 14px;
                font-weight: bold;
                text-align: center;
                padding: 10px 0;
                border-radius: 24px;
                width: 170px;
                margin: 14px auto 0 auto;
                box-shadow: 0 3px 6px rgba(0,0,0,0.12);
            }}
            .zone-clavier {{
                flex: 1;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(4, 1fr);
                padding: 10px 18px;
                background: white;
            }}
            .touche {{
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 28px;
                font-weight: 500;
                color: #1BA6C9;
            }}
            .touche-c {{
                color: #F0727A;
                font-weight: bold;
            }}
            .nav-bar {{
                height: 22px;
                background: white;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .home-indicator {{
                width: 90px;
                height: 4px;
                background: #94A3B8;
                border-radius: 2px;
            }}
        </style>
    </head>
    <body>
        <div class="phone-frame">
            <div class="notch"></div>
            <div class="status-bar">
                <span>12:00</span>
                <span>📶 🔋 100%</span>
            </div>
            
            <div class="zone-haut">
                <div class="titre-app">Currency Converter</div>

                <div class="row-devise">
                    <div class="spinner-box">{devise_source} ▼</div>
                    <div class="montant-display">{montant}</div>
                </div>

                <div class="btn-inverser">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="white">
                        <path d="M16 17.01V10h-2v7.01h-3L15 21l4-3.99h-3zM9 3L5 6.99h3V14h2V6.99h3L9 3z"/>
                    </svg>
                </div>

                <div class="row-devise">
                    <div class="spinner-box">{devise_cible} ▼</div>
                    <div class="montant-display" style="color: {'white' if resultat else 'transparent'};">{resultat if resultat else '0'}</div>
                </div>

                <div class="btn-convertir">CONVERTIR</div>
            </div>

            <div class="zone-clavier">
                <div class="touche">7</div>
                <div class="touche">8</div>
                <div class="touche">9</div>
                <div class="touche">4</div>
                <div class="touche">5</div>
                <div class="touche">6</div>
                <div class="touche">1</div>
                <div class="touche">2</div>
                <div class="touche">3</div>
                <div class="touche touche-c">C</div>
                <div class="touche">0</div>
                <div class="touche" style="font-weight: bold;">.</div>
            </div>

            {toast_html}

            <div class="nav-bar">
                <div class="home-indicator"></div>
            </div>
        </div>
    </body>
    </html>
    """

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 420, "height": 760})

        scenarios = [
            ("conv_01_demarrage.png", {"devise_source": "USD", "devise_cible": "EUR", "montant": "0", "resultat": ""}),
            ("conv_02_usd_eur.png", {"devise_source": "USD", "devise_cible": "EUR", "montant": "120", "resultat": "102.56"}),
            ("conv_03_eur_tnd.png", {"devise_source": "EUR", "devise_cible": "TND", "montant": "100", "resultat": "340.00"}),
            ("conv_04_gbp_usd.png", {"devise_source": "GBP", "devise_cible": "USD", "montant": "50", "resultat": "67.24"}),
            ("conv_05_eur_eur.png", {"devise_source": "EUR", "devise_cible": "EUR", "montant": "10", "resultat": "10.00"}),
            ("conv_06_erreur_zero.png", {"devise_source": "USD", "devise_cible": "EUR", "montant": "0", "resultat": "", "toast_msg": "Veuillez saisir un montant"}),
        ]

        for fname, kwargs in scenarios:
            html = get_converter_phone_html(**kwargs)
            page.set_content(html)
            outpath = os.path.join(SCREENSHOTS_DIR, fname)
            page.locator(".phone-frame").screenshot(path=outpath)
            print(f"Generated screenshot: {outpath}")

        browser.close()

if __name__ == "__main__":
    run()
