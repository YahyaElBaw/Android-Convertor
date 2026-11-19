import os
import base64
from playwright.sync_api import sync_playwright

def get_b64(path):
    with open(path, "rb") as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

def generate_pdf(html_content, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
        )
        browser.close()
    print(f"PDF generated: {output_path}")

BASE_CSS = """
    @page {
        size: A4;
        margin: 15mm;
        @bottom-right {
            content: counter(page);
        }
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; }
    body { color: #1E293B; line-height: 1.6; font-size: 13px; background: white; }
    h1 { color: #0F172A; font-size: 24px; margin-bottom: 8px; border-bottom: 2px solid #2BB8E8; padding-bottom: 6px; }
    h2 { color: #0284C7; font-size: 17px; margin-top: 18px; margin-bottom: 8px; border-bottom: 1px solid #E2E8F0; padding-bottom: 4px; }
    h3 { color: #334155; font-size: 14px; margin-top: 12px; margin-bottom: 4px; }
    p { margin-bottom: 8px; text-align: justify; }
    ul, ol { margin-left: 20px; margin-bottom: 10px; }
    li { margin-bottom: 4px; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; }
    .badge-green { background: #DCFCE7; color: #166534; }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
    .badge-red { background: #FEE2E2; color: #991B1B; }
    table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 12px; }
    th, td { border: 1px solid #CBD5E1; padding: 6px 10px; text-align: left; }
    th { background: #F1F5F9; color: #0F172A; font-weight: 600; }
    tr:nth-child(even) { background: #F8FAFC; }
    code { font-family: 'Consolas', monospace; background: #F1F5F9; color: #0284C7; padding: 2px 5px; border-radius: 4px; font-size: 12px; }
    pre { background: #0F172A; color: #F8FAFC; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 11px; line-height: 1.4; margin: 10px 0; font-family: 'Consolas', monospace; }
    .img-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 15px 0; }
    .img-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 8px; text-align: center; }
    .img-card img { width: 100%; max-height: 250px; object-fit: contain; border-radius: 6px; }
    .img-caption { font-size: 11px; font-weight: 600; color: #475569; margin-top: 6px; }
    .header-box { background: linear-gradient(135deg, #0284C7, #2BB8E8); color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .header-box h1 { color: white; border: none; font-size: 26px; }
    .header-meta { display: flex; gap: 20px; margin-top: 10px; font-size: 12px; opacity: 0.9; }
    .note-box { background: #F0F9FF; border-left: 4px solid #0284C7; padding: 10px 14px; border-radius: 4px; margin: 10px 0; }
    .page-break { page-break-before: always; }
"""

def create_convertor_compte_rendu():
    base_dir = r"D:/L3MDW/Mobile/Convertor/screenshots"
    img1 = get_b64(f"{base_dir}/conv_01_demarrage.png")
    img2 = get_b64(f"{base_dir}/conv_02_usd_eur.png")
    img3 = get_b64(f"{base_dir}/conv_03_eur_tnd.png")
    img4 = get_b64(f"{base_dir}/conv_04_gbp_usd.png")
    img5 = get_b64(f"{base_dir}/conv_05_eur_eur.png")
    img6 = get_b64(f"{base_dir}/conv_06_erreur_zero.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{BASE_CSS}</style>
    </head>
    <body>
        <div class="header-box">
            <h1>Compte Rendu de Réalisation — Currency Converter</h1>
            <p>Application Android Native en Kotlin de conversion de devises avec clavier personnalisé</p>
            <div class="header-meta">
                <span><strong>Projet :</strong> Currency Converter</span>
                <span><strong>Niveau :</strong> Débutant L3 MDW</span>
                <span><strong>Architecture :</strong> ConstraintLayout + TableLayout</span>
                <span><strong>Status :</strong> Validé (100%)</span>
            </div>
        </div>

        <h2>1. Présentation de l'Application</h2>
        <p>L'application <strong>Currency Converter</strong> permet de convertir un montant d'une devise vers une autre à partir de taux fixes avec l'Euro (EUR) comme devise pivot. L'interface est scindée en deux zones distinctes : une zone d'affichage supérieure sur fond bleu turquoise (#2BB8E8) et un clavier numérique personnalisé intégré au bas de l'écran.</p>

        <div class="note-box">
            <strong>Règles de gestion et contraintes implémentées :</strong>
            <ul>
                <li>Saisie exclusive via le clavier personnalisé (touches 0 à 9, '.' et 'C').</li>
                <li>Montant limité à 10 caractères et au plus un seul point décimal.</li>
                <li>Bouton d'inversion qui permute instantanément les deux devises et recalcule si un résultat est déjà affiché.</li>
                <li>Devises gérées : USD, EUR, TND, GBP, JPY, CAD via un <code>ArrayAdapter</code> sur <code>R.array.devises</code>.</li>
                <li>Gestion d'erreur par Toast : « Veuillez saisir un montant » si l'utilisateur tente de convertir 0.</li>
            </ul>
        </div>

        <h2>2. Galerie des Vues et Cas de Test de l'Application</h2>
        <div class="img-grid">
            <div class="img-card">
                <img src="{img1}" alt="Démarrage" />
                <div class="img-caption">Vue 1 : Démarrage (USD &rarr; EUR, Montant 0)</div>
            </div>
            <div class="img-card">
                <img src="{img2}" alt="USD vers EUR" />
                <div class="img-caption">Vue 2 : 120 USD &rarr; EUR = 102.56</div>
            </div>
            <div class="img-card">
                <img src="{img3}" alt="EUR vers TND" />
                <div class="img-caption">Vue 3 : 100 EUR &rarr; TND = 340.00</div>
            </div>
        </div>

        <div class="img-grid">
            <div class="img-card">
                <img src="{img4}" alt="GBP vers USD" />
                <div class="img-caption">Vue 4 : 50 GBP &rarr; USD = 67.24</div>
            </div>
            <div class="img-card">
                <img src="{img5}" alt="EUR vers EUR" />
                <div class="img-caption">Vue 5 : 10 EUR &rarr; EUR = 10.00</div>
            </div>
            <div class="img-card">
                <img src="{img6}" alt="Erreur Montant 0" />
                <div class="img-caption">Vue 6 : Alerte Toast si montant = 0</div>
            </div>
        </div>

        <div class="page-break"></div>

        <h2>3. Tableau de Validation des Tests</h2>
        <table>
            <thead>
                <tr>
                    <th>Montant</th>
                    <th>Source</th>
                    <th>Cible</th>
                    <th>Résultat attendu</th>
                    <th>Résultat obtenu</th>
                    <th>Statut</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>120</td>
                    <td>USD</td>
                    <td>EUR</td>
                    <td>102.56</td>
                    <td>102.56</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>100</td>
                    <td>EUR</td>
                    <td>TND</td>
                    <td>340.00</td>
                    <td>340.00</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>50</td>
                    <td>GBP</td>
                    <td>USD</td>
                    <td>67.24</td>
                    <td>67.24</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>10</td>
                    <td>EUR</td>
                    <td>EUR</td>
                    <td>10.00</td>
                    <td>10.00</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
                <tr>
                    <td>0</td>
                    <td>USD</td>
                    <td>EUR</td>
                    <td>Toast d'erreur</td>
                    <td>"Veuillez saisir un montant"</td>
                    <td><span class="badge badge-green">SUCCÈS</span></td>
                </tr>
            </tbody>
        </table>

        <h2>4. Détails Techniques</h2>
        <p>Le projet est composé des modules :</p>
        <ul>
            <li><code>CurrencyConverter.kt</code> : Classe singleton contenant la table des taux fixes et l'algorithme pivot Euro.</li>
            <li><code>MainActivity.kt</code> : Contrôleur gérant les clics du clavier personnalisé, la construction des chaînes numériques, les liaisons ViewBinding et l'inversion des Spinners.</li>
            <li><code>activity_main.xml</code> : Layout divisé avec précision (ConstraintLayout 46% supérieur + TableLayout 54% inférieur).</li>
            <li>Orientation forcée en mode portrait via <code>android:screenOrientation="portrait"</code> dans le manifest.</li>
        </ul>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\Convertor\Compte_Rendu_Convertisseur.pdf")

def create_convertor_guide_etudiant():
    base_dir = r"D:/L3MDW/Mobile/Convertor/screenshots"
    img1 = get_b64(f"{base_dir}/conv_02_usd_eur.png")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{BASE_CSS}</style>
    </head>
    <body>
        <div class="header-box">
            <h1>Guide Étudiant : Création du Convertisseur de Devises</h1>
            <p>Apprendre les Spinners, le View Binding, et concevoir un clavier virtuel avec TableLayout</p>
            <div class="header-meta">
                <span><strong>Projet #3 :</strong> Currency Converter</span>
                <span><strong>Niveau :</strong> Débutant / Étudiant</span>
                <span><strong>Composants Clés :</strong> Spinner, ArrayAdapter, TableLayout</span>
            </div>
        </div>

        <h2>1. Présentation du TP</h2>
        <p>Dans ce troisième projet, vous allez concevoir une application de conversion monétaire. Contrairement aux applications classiques qui utilisent le clavier virtuel du système Android, nous allons ici fabriquer notre propre <strong>clavier tactile virtuel</strong> avec un <code>TableLayout</code>, et alimenter des menus déroulants (<code>Spinner</code>) à l'aide d'un adaptateur de données (<code>ArrayAdapter</code>).</p>

        <div style="display: flex; gap: 20px; align-items: center; margin: 15px 0;">
            <div style="flex: 1;">
                <p><strong>La formule de conversion avec pivot Euro :</strong></p>
                <div style="background: #F0F9FF; border: 1px solid #BAE6FD; padding: 10px; border-radius: 6px; font-size: 13px; font-weight: bold; color: #0369A1;">
                    1. Montant en EUR = Montant / Taux(Source)<br>
                    2. Résultat Final = Montant en EUR &times; Taux(Cible)
                </div>
                <p style="margin-top: 10px;">Exemple : Pour convertir 120 USD en EUR :<br>
                <code>120 / 1.17 &times; 1.00 = 102.56 EUR</code>.</p>
            </div>
            <div style="width: 140px; text-align: center;">
                <img src="{img1}" style="width: 130px; border-radius: 8px; border: 1px solid #CBD5E1;" alt="Converter preview" />
            </div>
        </div>

        <h2>2. Les Notions Clés Expliquées</h2>
        <ul>
            <li><strong>Le Spinner :</strong> C'est la liste déroulante d'Android. Il permet à l'utilisateur de sélectionner un élément parmi plusieurs choix (ici les monnaies).</li>
            <li><strong>L'ArrayAdapter :</strong> Un adaptateur qui prend une collection de données (par exemple un tableau de chaînes défini dans <code>strings.xml</code>) et crée les vues graphiques à insérer dans le Spinner.</li>
            <li><strong>Le TableLayout :</strong> Une disposition sous forme de grille organisée en lignes (<code>TableRow</code>) et colonnes. Idéal pour concevoir des claviers de calculatrices ou de pavés numériques.</li>
            <li><strong>La Map en Kotlin :</strong> Une collection de paires clé/valeur associant le code de la devise (String) à son taux (Double).</li>
        </ul>

        <div class="page-break"></div>

        <h2>3. Étapes de Réalisation Pas à Pas</h2>

        <h3>Étape 1 : Déclarer la liste des devises dans strings.xml</h3>
        <p>Dans <code>res/values/strings.xml</code>, nous créons un <code>&lt;string-array&gt;</code> contenant nos 6 devises :</p>
        <pre>&lt;string-array name="devises"&gt;
    &lt;item&gt;USD&lt;/item&gt;
    &lt;item&gt;EUR&lt;/item&gt;
    &lt;item&gt;TND&lt;/item&gt;
    &lt;item&gt;GBP&lt;/item&gt;
    &lt;item&gt;JPY&lt;/item&gt;
    &lt;item&gt;CAD&lt;/item&gt;
&lt;/string-array&gt;</pre>

        <h3>Étape 2 : Lier le Spinner avec l'ArrayAdapter en Kotlin</h3>
        <pre>val adapter = ArrayAdapter.createFromResource(
    this,
    R.array.devises,
    android.R.layout.simple_spinner_item
)
adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)

binding.spDeviseSource.adapter = adapter
binding.spDeviseCible.adapter = adapter

// Valeurs par défaut : USD en source et EUR en cible
binding.spDeviseSource.setSelection(0)
binding.spDeviseCible.setSelection(1)</pre>

        <h3>Étape 3 : Gérer la saisie sur le clavier virtuel</h3>
        <p>Chaque pression sur une touche numérique appelle <code>ajouterCaractere(c)</code> en appliquant les contrôles de validité :</p>
        <pre>private fun ajouterCaractere(c: String) {{
    val texteActuel = binding.tvMontant.text.toString()

    // Règle 1 : Limite de 10 caractères
    if (texteActuel.length >= 10) return

    // Règle 2 : Un seul point décimal
    if (c == "." && texteActuel.contains(".")) return

    // Règle 3 : Le premier chiffre tapé remplace le "0"
    binding.tvMontant.text = if (texteActuel == "0" && c != ".") c else texteActuel + c
}}</pre>

        <h3>Étape 4 : Le Bouton d'Inversion</h3>
        <p>Pour échanger instantanément les deux devises au clic sur l'icône, nous inversons simplement leurs positions dans les Spinners :</p>
        <pre>val posSource = binding.spDeviseSource.selectedItemPosition
val posCible = binding.spDeviseCible.selectedItemPosition

binding.spDeviseSource.setSelection(posCible)
binding.spDeviseCible.setSelection(posSource)</pre>

        <h2>4. Pièges à Éviter pour les Étudiants</h2>
        <div class="note-box">
            <ul>
                <li><strong>Division par zéro :</strong> Vérifiez toujours que le taux de la devise n'est pas nul.</li>
                <li><strong>Changement de devise identique :</strong> Si l'utilisateur choisit USD &rarr; USD, le résultat doit être exactement égal au montant sans lever d'erreur.</li>
                <li><strong>Formatage :</strong> Utilisez toujours <code>String.format(Locale.US, "%.2f", resultat)</code> pour forcer le point décimal et 2 chiffres après la virgule.</li>
            </ul>
        </div>
    </body>
    </html>
    """
    generate_pdf(html, r"D:\L3MDW\Mobile\pdfs\03_Guide_Etudiant_Convertisseur_Devises.pdf")

if __name__ == "__main__":
    create_convertor_compte_rendu()
    create_convertor_guide_etudiant()
