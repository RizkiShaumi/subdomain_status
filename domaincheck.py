import requests
import csv

# List of subdomains to check
subdomains = [
"absen.garutkab.go.id",
        "satudata.archive.garutkab.go.id",
        "bakesbangpol.garutkab.go.id",
        "bapenda.garutkab.go.id",
        "app.bapenda.garutkab.go.id",
        "cloud.bapenda.garutkab.go.id",
        "dashboard.bapenda.garutkab.go.id",
        "e-pbb.bapenda.garutkab.go.id",
        "epad.bapenda.garutkab.go.id",
        "esptpd.bapenda.garutkab.go.id",
        "ewasdal.bapenda.garutkab.go.id",
        "potensi.bapenda.garutkab.go.id",
        "sirojak.bapenda.garutkab.go.id",
        "siwardah.bapenda.garutkab.go.id",
        "bappeda.garutkab.go.id",
        "dewamembumi.bappeda.garutkab.go.id",
        "sipinter.bappeda.garutkab.go.id",
        "spdewamembumi.bappeda.garutkab.go.id",
        "baznas.garutkab.go.id",
        "bkd.garutkab.go.id",
        "cpanel.bkd.garutkab.go.id",
        "sikopi-garut.bkd.garutkab.go.id",
        "simasn.bkd.garutkab.go.id",
        "simnonasn.bkd.garutkab.go.id",
        "bpbd.garutkab.go.id",
        "infolaras.bpbd.garutkab.go.id",
        "sikat.bpbd.garutkab.go.id",
        "cascading.garutkab.go.id",
        "cloud.garutkab.go.id",
        "commandcenter.garutkab.go.id",
        "covid19.garutkab.go.id",
        "cpanel.garutkab.go.id",
        "siphp.damkar.garutkab.go.id",
        "dinkes.garutkab.go.id",
        "ditakesmas.dinkes.garutkab.go.id",
        "dippda.garutkab.go.id",
        "disdik.garutkab.go.id",
        "sipantas.disdik.garutkab.go.id",
        "diskannak.garutkab.go.id",
        "e-yanlikdiskannak.diskannak.garutkab.go.id",
        "tpi.diskannak.garutkab.go.id",
        "asik.diskominfo.garutkab.go.id",
        "did.diskominfo.garutkab.go.id",
        "helpdesk.diskominfo.garutkab.go.id",
        "api.helpdesk.diskominfo.garutkab.go.id",
        "silakop.diskopukm.garutkab.go.id",
        "sipendekar.diskopukm.garutkab.go.id",
        "disnakertrans.garutkab.go.id",
        "gentrakarya.disnakertrans.garutkab.go.id",
        "oncase.disnakertrans.garutkab.go.id",
        "sijonmantap.disnakertrans.garutkab.go.id",
        "siparkit.disnakertrans.garutkab.go.id",
        "disparbud.garutkab.go.id",
        "api.disparbud.garutkab.go.id",
        "codiad.disparbud.garutkab.go.id",
        "serasi.disparbud.garutkab.go.id",
        "serasi-api.disparbud.garutkab.go.id",
        "siapdol.disparbud.garutkab.go.id",
        "sipaku.disparbud.garutkab.go.id",
        "tirek.disparbud.garutkab.go.id",
        "tirex.disparbud.garutkab.go.id",
        "industri.disperindag.garutkab.go.id",
        "rumahekspor.disperindag.garutkab.go.id",
        "disperkim.garutkab.go.id",
        "proposal.disperkim.garutkab.go.id",
        "rutilahu.disperkim.garutkab.go.id",
        "siduru.disperkim.garutkab.go.id",
        "sikumpay.disperkim.garutkab.go.id",
        "simdisperkim.disperkim.garutkab.go.id",
        "surat.disperkim.garutkab.go.id",
        "dispusip.garutkab.go.id",
        "simpan-online.dispusip.garutkab.go.id",
        "api-siram.distan.garutkab.go.id",
        "siram.distan.garutkab.go.id",
        "dlh.garutkab.go.id",
        "siladu.dlh.garutkab.go.id",
        "dodol.garutkab.go.id",
        "dpmpt.garutkab.go.id",
        "dpmptsp.garutkab.go.id",
        "simadu-mpp.dpmptsp.garutkab.go.id",
        "aksifaster.dprd.garutkab.go.id",
        "jdih.dprd.garutkab.go.id",
        "e-litbang.garutkab.go.id",
        "eoffice.garutkab.go.id",
        "admin.esurat.garutkab.go.id",
        "gitlab.garutkab.go.id",
        "inspektorat.garutkab.go.id",
        "dumas.inspektorat.garutkab.go.id",
        "jdih.garutkab.go.id",
        "kec-cisompet.garutkab.go.id",
        "kec-kadungora.garutkab.go.id",
        "www.siomcakap.kec-kadungora.garutkab.go.id",
        "kec-karangtengah.garutkab.go.id",
        "simansur.kec-karangtengah.garutkab.go.id",
        "siotamtiba.kec-karangtengah.garutkab.go.id",
        "sipapabb.kec-karangtengah.garutkab.go.id",
        "sippedas.kec-karangtengah.garutkab.go.id",
        "sippede.kec-karangtengah.garutkab.go.id",
        "siladuketan.kec-malangbong.garutkab.go.id",
        "kec-samarang.garutkab.go.id",
        "smart-takida.kec-tarogongkidul.garutkab.go.id",
        "kotawetan.garutkab.go.id",
        "mail.garutkab.go.id",
        "mediacenter.garutkab.go.id",
        "minio.garutkab.go.id",
        "api.mpp.garutkab.go.id",
        "panel.mpp.garutkab.go.id",
        "ns1.garutkab.go.id",
        "ns2.garutkab.go.id",
        "pandu-online.garutkab.go.id",
        "pastioke.garutkab.go.id",
        "pic.garutkab.go.id",
        "pkm-cikelet.garutkab.go.id",
        "simpus.pkm-kersamenak.garutkab.go.id",
        "ppid.garutkab.go.id",
        "pupr.garutkab.go.id",
        "ampe-retak.pupr.garutkab.go.id",
        "ams.pupr.garutkab.go.id",
        "datacenter.pupr.garutkab.go.id",
        "pi.pupr.garutkab.go.id",
        "sijanda.pupr.garutkab.go.id",
        "sijantan.pupr.garutkab.go.id",
        "sikojantan.pupr.garutkab.go.id",
        "simanpro.pupr.garutkab.go.id",
        "simolek.pupr.garutkab.go.id",
        "siperaba.pupr.garutkab.go.id",
        "rsud.garutkab.go.id",
        "app.rsud.garutkab.go.id",
        "rsudrslamet.garutkab.go.id",
        "s3-yanlik.garutkab.go.id",
        "sakip.garutkab.go.id",
        "satudata.garutkab.go.id",
        "satudata-api.garutkab.go.id",
        "sidat-kakap.garutkab.go.id",
        "sidogar.garutkab.go.id",
        "sievka.garutkab.go.id",
        "sijempol.garutkab.go.id",
        "sikd.garutkab.go.id",
        "simap-disdik.garutkab.go.id",
        "simasn.garutkab.go.id",
        "simpangan.garutkab.go.id",
        "simpangan-api.garutkab.go.id",
        "sipkd.garutkab.go.id",
        "siraja.garutkab.go.id",
        "siska.garutkab.go.id",
        "sitel.garutkab.go.id",
        "renaksi.spbe.garutkab.go.id",
        "tp4d.garutkab.go.id",
        "vaksin.garutkab.go.id",
        "visitgarut.garutkab.go.id",
        "wbs.garutkab.go.id",
        "webmail.garutkab.go.id",
        "whm.garutkab.go.id",
        "www.garutkab.go.id"
    ]

def check_subdomain(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        if response.status_code == 200:
            return 'Active'
        else:
            return 'Inactive'
    except requests.RequestException as e:
        return 'Inactive'

# Open CSV file for writing
try:
    with open('C:/Users/Admin/Documents/Magan/subdomain_status_fix.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subdomain', 'Status'])

        # Check each subdomain and write the result to CSV
        for subdomain in subdomains:
            status = check_subdomain(subdomain)
            writer.writerow([subdomain, status])

    print("Subdomain status has been saved to subdomain_status.csv")

except IOError as e:
    print(f"Error writing to file: {e}")
