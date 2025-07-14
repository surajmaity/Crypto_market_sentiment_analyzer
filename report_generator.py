from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def generate_html_report(data, template_name='report.html', output_filename='crypto_report.html'):
    """
    Generates an HTML report from a template and data.
    """
    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template(template_name)

    report_context = {
        'cryptos': data,
        'report_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    }

    html_content = template.render(report_context)

    with open(output_filename, 'w') as f:
        f.write(html_content)
    
    print(f"Report generated successfully: {output_filename}")