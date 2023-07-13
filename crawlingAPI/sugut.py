import requests
import pandas as pd

url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"

res = []
for x in range(1,5):
    querystring = {"isProductNeeded":"true","pageSize":"100","responseFormat":"json","currency":"USD","catalogId":"20602","viewTaskName":"CategoryDisplayView","storeId":"10152","langId":"-1","categoryId":"3074457345626651837","pageView":"image","currentPage":f"{x}"}


    headers = {
    "cookie": "aka-cc=ID; aka-ct=JAKARTA; aka-zp=; bm_sz=30774CB50F7343F99249EA3379676621~YAAQQv5eb2FKvCiJAQAAA8xZLhRElAKKxrwuC+Zy9qMJlituWZIbFat9xcSPoQYJ8+jpcUUD/O4zvylzMVDywsG7btaZVTHb/GKV2MNoqjy3KKVEV8+KCuMGVfB7FjIhlzBIfdABh0ZuPFWWUZ0FNM/OPyN12vrGswi+dZu2o4gp5IqfzNDSJ8+rYBPQq4qzXZt6TrP6HL3Rdk3T3DRda1tID7r2h+IsJQLHrrTFz8Y2qY/u/STtbqClPL+Qpwy66H7I6ehUyZqElRAG/E+HPiShr9fgD+Z5PpRySzA//jzX3MB29+EpKw==~3422004~3748661; mt.v=2.659803543.1688699804145; SGPF=31FQVQktaEQZFs3PyihlZJJuFFiLi7V6P9FTD25U_RzBtKYyvtcQKbA; dtCookie=v_4_srv_-2D99_sn_1DARAUUNQI5DMUDVIUEJP14CHSREQ92R; rxVisitor=16886998041992VKO3B9QRL82KNAAPCP68FVO4CAKOG1J; sgh-desktop-facet-state-search=; dtSa=-; ftr_ncd=6; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=google.com/; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=google.com/; tealium_data_session_timeStamp=1688699804707; userToken=undefined; TrafficSource_Override=1; tiktok_click_id=undefined; __wid=294142708; ftr_blst_1h=1688699804741; AMCVS_125138B3527845350A490D4C^%^40AdobeOrg=1; ak_bmsc=BEA77DF514A9E07107DEEDB639FC5DD3~000000000000000000000000000000~YAAQQv5eb5VLvCiJAQAARnpaLhTjha1+SBY11cbcMrOe1n+2YQuhqUkEjnPwgWSSIGWk/4bKHFykpOgwEcWX3dXQOZdiYS2TNx0RY8TCO1wuVUIomi30kazslrirxZ7GHcsu6jalvLanQNi6V+qBPaeiopmFW7H5N6yjWV2bt/CQn0m8gHPUM+L+lS8ELpOSYafFud+9ASBDCntjNHDHdouifz+7HQnaVH2Irf07WyKQCHb4MoNIX0s3tJPTWMZXSMDbtRj5rz3UEp7iimyTpxQZx0n0oUaSSe5w8pejwBiKl6ndBaH+5f/evBofCkbkSL6LhhCTT95sHhJXlzpxu6NQE5n30fOEtNvEbQDLTLgH1cS35+vFww7YCG5znhB9J4buigevDXeZoue/TjyZMFefbyKy8xHLkElHnzuuY//6ia1MlPO51gyKzeZ8ZJ2nlMAnX4V8QoXtEu0if9bDlUU7fCPgEUik8643BhH4c5VK0JdUa+C1Y3J3n8WISUU5; s_ecid=MCMID^%^7C47763489189574986172296367749579922961; AMCV_125138B3527845350A490D4C^%^40AdobeOrg=-1303530583^%^7CMCIDTS^%^7C19546^%^7CMCMID^%^7C47763489189574986172296367749579922961^%^7CMCAAMLH-1689304604^%^7C3^%^7CMCAAMB-1689304604^%^7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y^%^7CMCOPTOUT-1688707004s^%^7CNONE^%^7CMCAID^%^7CNONE^%^7CvVersion^%^7C3.3.0; JSESSIONID=0000nW8hnKxKmi3b2hQKX88u0P1:1c7qtngmi; TS011f624f=015966d292d91156f979fb058516f0df76d18588cfeabdafeec67d0a9da0830f3d9fa3bae65aabbbc71d1c0c70afb5ff96856692a6a38fba9f763b104bb3bfe2dc187a7377; s_cc=true; _abck=41D2567A98D579BE293A3D921BB9D69D~0~YAAQQv5eb51LvCiJAQAArn1aLgqMqq4Q1IIHg9JpCtp9eZY3FkttKokQcdKrWK9HXAZpA2sL1PQBB0k07bqBKW9i0W37+Z2tcp/PtMBLp/LND4/4bNCIyefdCkfMONfedjhL1YJgRF2eo/zopARs6g48dTntIAr4XtxGFLhgsEpvJ7O6Ozcne/ufN1hIOHaVjwi7EHgL2QbG1Y2c3sNBvag8fJFBfeW05vKpSzXx5uDlatgHH9bmBTr++TpAg1lYKkxaZNlXQXP9fK2WlhWfdsDntqs3Mh+wc5nLdT4FoD0vFVPFZNAnc097yC5akGvWk/oiHKJdlbE7/lk+mDzEOErwsOQzp9f4mQO8+6IIw+xAilYP2LqyzfZcamzxBPzATCBK3jIJugaUEvGlUbB9bW1httuXnF5KhlmDFgg=~-1~^|^|-1^|^|~-1; UserTrackingProducts=0; CONSENTMGR=consent:true^%^7Cts:1688699808231; _cs_mk_aa=0.9886235652226241_1688699808283; _cs_c=1; _gcl_au=1.1.326039999.1688699808; _ga=GA1.1.811834502.1688699809; _scid=fa44bfd6-78fd-40a8-90ef-fa9964e148ba; _fbp=fb.1.1688699808987.2053501851; _tt_enable_cookie=1; _ttp=CqFeiya_d40pI4TKY4FGnlDm6Md; smc_uid=1688699809560233; smc_tag=eyJpZCI6Njc4LCJuYW1lIjoic3VuZ2xhc3NodXQuY29tIn0=; smc_session_id=gUTPt5Dk8m2yyQ32IgwbpFbVnAWp8Xfa; _sctr=1^%^7C1688662800000; outbrain_cid_fetch=true; tfpsi=41d5f5a9-f11b-47fb-905b-082651ebfa7c; smc_refresh=24860; _pin_unauth=dWlkPU5qRTROV000TW1VdE5EQXlZeTAwTjJKakxXSmtaVGN0TjJZeE5qbGpPR0ZoWldVMg; smc_sesn=1; smc_not=default; dtLatC=2; sgh-desktop-facet-state-plp=categoryid:undefined^|gender:true^|brands:partial^|polarized:true^|price:true^|frame-shape:partial^|color:true^|face-shape:false^|fit:false^|materials:false^|lens-treatment:false; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=307072ORG; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=307071ORG-307072ORG; _cs_id=84671eec-4077-a632-9612-16fdc37e06f4.1688699808.1.1688699875.1688699808.1.1722863808475; _cs_s=2.0.0.1688701675330; _scid_r=fa44bfd6-78fd-40a8-90ef-fa9964e148ba; _uetsid=b5d740901c7411eeadb6492d8b13cf1c; _uetvid=b5d889701c7411ee9e899718f89f60c6; _derived_epik=dj0yJnU9cWVkMWI4RGNWNWhOYmhqSzJsOHdUR2MwWVFaMWFmQ0Umbj1uR0FkeTBXNUhBSGxibTFzSURFRkxnJm09MSZ0PUFBQUFBR1NuZ19zJnJtPTEmcnQ9QUFBQUFHU25nX3Mmc3A9Mg; cto_bundle=SMUPkF9rc3JzRUh4YnlzUGRENjcxdDRhU2x1UFlzWVloOE1BWjl1TzNva0NMNWtScmlPeU1CTktZWTFGWFZsQmxoOE1INzJGTjFiUEJvdDVSWCUyRjdja0JSRWVDY1AlMkYxN1JXZld6Nk9vUnI0MWRQZ3ZVandTUXBmZEpOdnBYJTJCY2NEbzduUXM1NkEwN2lQdGRwYnJzd1JCRHptNVElM0QlM0Q; forterToken=9c60272bfba443ea971db475d01b7b38_1688699874061__UDF43-m4_6; rxvt=1688701677306^|1688699804200; dtPC=-99^-vPQEBQALGSUKDCJAHNQFCUDKJAFTRWVRM-0e0; tealium_data_action_lastAction=Men:Sun:Plp click ^[sgh-load-more  button^]^[Loadmoresunglasses^]; tealium_data_action_lastEvent=click ^[sgh-load-more  button^]^[Loadmoresunglasses^]; s_sq=^%^5B^%^5BB^%^5D^%^5D; bm_sv=F6B1197C1873B121B04CB69AA4E4F8D4~YAAQQv5eb0dQvCiJAQAAU5NcLhR5aWmiy39d2AZ84o52LDM4WpjXGjwsNGYd0fbzac6lN6poVGQwzxjmIn0ArpjMeuKY5LZpJkVthTyXDgV+iZg07FB/VhlMKYwqtjTcvwCoONe6viH3y+MAFh/yBPidavdwUY8/FGeSBxdwhanLvWYVRaLIoMw6a7PiJ1JRksMLZJG0K486sxoMJ9xMdooI40wxBxmyzOtzGNaTZX2TFBp3WiRRKl0r+yHpdEq+pdWqWYY=~1; _ga_6P80B86QTY=GS1.1.1688699808.1.1.1688699943.56.0.0; smc_tpv=4; smc_spv=4; smct_session=^{^\^s^^:1688699810593,^\^l^^:1688699988991,^\^lt^^:1688699988991,^\^t^^:142,^\^p^^:36^}; utag_main=v_id:01892e5a1c18000f28c5b98a735f0506f002e06700978^n:1^e:12^s:0^t:1688701789731^:1688699804696^%^3Bexp-session^n:2^%^3Bexp-session^:sunglasshut.com^:1^:2^%^3Bexp-session^:ap-east-1^%^3Bexp-session",
    "authority": "www.sunglasshut.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://www.sunglasshut.com/us/mens-sunglasses?currentPage=2",
    "sec-ch-ua": "^\^Not.A/Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^114^^, ^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

    r = requests.request("GET", url, headers=headers, params=querystring)

    data = r.json()
    for p in data['plpView']['products']['products']['product']:
        res.append(p)
        
df = pd.json_normalize(res)

df.to_csv('secondresult.csv')
