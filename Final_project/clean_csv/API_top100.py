from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Charger le CSV dans un DataFrame
df = pd.read_csv("Web_Scrapping.csv")

# Transformation du market cap
df['market_cap_value'] = df['market_cap'].replace({'\$': '', 'B': 'e9', 'M': 'e6'}, regex=True).apply(pd.eval).astype(float)
df['market_cap_unit'] = df['market_cap'].str.extract(r'([A-Za-z]+)')

# Créer df_top100 avec les colonnes 'position', 'country', 'company_name' et 'market_cap_value'
df_top100 = df[['position', 'country', 'company_name', 'market_cap_value']]

# Fonction de recherche d'une entreprise dans le top 100
@app.route('/api/company', methods=['GET'])
def get_company_info():
    company_name = request.args.get('company_name')  # Récupérer le nom de l'entreprise depuis les paramètres GET

    # Recherche de l'entreprise dans le DataFrame
    company = df_top100[df_top100['company_name'].str.contains(company_name, case=False, na=False)]

    if company.empty:
        return jsonify({"message": "Sorry, but it's not a company part of the top 100"}), 404

    # Retourner les informations si l'entreprise est trouvée
    company_info = company.iloc[0]  # Si plusieurs résultats sont trouvés, on prend le premier
    return jsonify({
        "position": company_info['position'],
        "country": company_info['country'],
        "company_name": company_info['company_name'],
        "market_cap_value": company_info['market_cap_value']
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)



