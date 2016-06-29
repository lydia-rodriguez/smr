from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    connection = engine.connect()

    client_id = ''
    client_name = ''
    site_name = ''
    mailfrom_lwr = mailfrom.lower()

    print(mailfrom_lwr)

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == mailfrom_lwr)

    try:
        with engine.connect() as conn:
            results_client_id = conn.execute(client_id_mailfrom).fetchall()
            ## some code
            # b = results_client_id.fetchall()
            # c = b[0]
            # client_id_dict = dict(zip(c.keys(), c.values()))
            # for key, value in client_id_dict.items():
            #     k = key
            #     client_id = int(value)
            for client_id in results_client_id:
                print(int(client_id))
                # print(key, client_id)
    except IndexError:
        print("Client ID not found using mailfrom.")
    #
    #     client_name_select = select([Client.client_name])
    #
    #     try:
    #         with engine.connect() as conn:
    #             results_client_nm = conn.execute(client_nm).fetchall()
    #             ## some code
    #             for client in results_client_nm:
    #                 client = (str(client[0]).lower())
    #                 if mailfrom_lwr.count(client) > 0:
    #                     client_name = str(client.encode('utf-8'))
    #                     break
    #                 else:
    #                     client_syn1 = select([Client.synonym1])
    #                     try:
    #                         with engine.connect() as conn_syn1:
    #                             results_client_syn1 = conn_syn1.execute(client_syn1).fetchall()
    #                             ## some code
    #                             for syn1 in results_client_syn1:
    #                                 syn1 = str(syn1[0]).lower()
    #                                 if mailfrom_lwr.count(syn1) > 0:
    #                                     print("syn found")
    #                                     client_syn_name = select([Client.client_name]).where(Client.synonym1 == syn1)
    #                                     with engine.connect() as conn_clientName:
    #                                         results_client_name
    #                                     b = client_syn_name.fetchall()
    #                                     c = b[0]
    #                                     client_name_dict = dict(zip(c.keys(), c.values()))
    #                                     for key, value in client_name_dict.items():
    #                                         client_name = str(value.encode('utf-8'))
    #
    #                                     client_name = str(client_syn_name.encode('utf-8'))
    #                                     break
    #                     except IndexError:
    #                         # client_syn1 = select([Client.synonym1])
    #                         # try:
    #                         print("fail")
    #     except IndexError:
    #         print("FAIL")
    #
    # if len(client_name) > 0:
    #     print("Client Found: " + str(client_name))
    #
    #     # Use this query to test if client_id value is found in sites table and output site_name.
    #
    #     try:
    #         client_sites = select([Site.site_name]).where(Site.client_id == int(client_id))
    #         with engine.connect() as conn:
    #             results_site_id = conn.execute(client_sites)
    #             ## some code
    #             b = results_site_id.fetchall()
    #             c = b[0]
    #             site_name_dict = dict(zip(c.keys(), c.values()))
    #             for key, value in site_name_dict.items():
    #                 k = key
    #                 site_name = str(value.encode('utf-8'))
    #                 # print(key, site_name)
    #         if len(site_name) > 0:
    #             print("Site Found: " + str(site_name))
    #         else:
    #             print("Site not found.")
    #     except:
    #         print("Site not found.")

    else:
        print("Client not found.")
