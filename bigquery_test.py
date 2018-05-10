from google.cloud import bigquery


def query_stackoverflow():
    client = bigquery.Client.from_service_account_json('./apikey.json')
    query_job = client.query("""
        SELECT * FROM `mercari-cdn:fastly.waf_mercari_dot_com_20180509`
        LIMIT 10""")

    results = query_job.result()
    print(results)
    for row in results:
        print(row)
        print("{} : {} views".format(row.url, row.view_count))


if __name__ == '__main__':
    query_stackoverflow()

