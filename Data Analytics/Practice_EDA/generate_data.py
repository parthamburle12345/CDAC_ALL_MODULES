import os
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_all_data(output_dir="d:/Engineering/CDAC_ALL_MODULES/Data Analytics/Practice_EDA/data"):
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(42)

    num_customers = 3500
    num_orders = 15000
    num_products = 80
    num_sessions = 25000

    print("Generating Customers...")
    customer_ids = [f"CUST-{i:05d}" for i in range(1, num_customers + 1)]
    
    channels = ['Organic Search', 'Paid Ads', 'Social Media', 'Referral', 'Email']
    channel_probs = [0.30, 0.25, 0.20, 0.15, 0.10]
    cust_channels = np.random.choice(channels, size=num_customers, p=channel_probs)
    
    segments = ['Consumer', 'Corporate', 'Small Business']
    cust_segments = np.random.choice(segments, size=num_customers, p=[0.70, 0.20, 0.10])
    
    states_meta = [
        ('CA', 'Los Angeles', 34.0522, -118.2437),
        ('CA', 'San Francisco', 37.7749, -122.4194),
        ('NY', 'New York City', 40.7128, -74.0060),
        ('TX', 'Houston', 29.7604, -95.3698),
        ('TX', 'Austin', 30.2672, -97.7431),
        ('IL', 'Chicago', 41.8781, -87.6298),
        ('WA', 'Seattle', 47.6062, -122.3321),
        ('FL', 'Miami', 25.7617, -80.1918),
        ('MA', 'Boston', 42.3601, -71.0589),
        ('CO', 'Denver', 39.7392, -104.9903),
        ('AZ', 'Phoenix', 33.4484, -112.0740),
        ('PA', 'Philadelphia', 39.9526, -75.1652)
    ]
    
    chosen_meta_idx = np.random.choice(len(states_meta), size=num_customers)
    cust_states = [states_meta[i][0] for i in chosen_meta_idx]
    cust_cities = [states_meta[i][1] for i in chosen_meta_idx]
    cust_lats = [states_meta[i][2] + np.random.normal(0, 0.08) for i in chosen_meta_idx]
    cust_lons = [states_meta[i][3] + np.random.normal(0, 0.08) for i in chosen_meta_idx]
    
    start_date = datetime(2023, 1, 1)
    signup_deltas = np.random.randint(0, 365, size=num_customers)
    cust_signups = [start_date + timedelta(days=int(d)) for d in signup_deltas]
    
    # A/B test variant assignment
    ab_variants = np.random.choice(['control', 'treatment_new_ui'], size=num_customers, p=[0.5, 0.5])
    
    # Policy treatment region: CA, NY, TX rolled out the new dynamic fulfillment policy
    treatment_regions = [1 if st in ['CA', 'NY', 'TX'] else 0 for st in cust_states]
    
    # Income bracket with MNAR (high-income individuals disproportionately decline to answer)
    raw_incomes = np.random.choice(['Low', 'Medium', 'High'], size=num_customers, p=[0.35, 0.45, 0.20])
    incomes_with_mnar = []
    for inc in raw_incomes:
        if inc == 'High' and np.random.rand() < 0.45:
            incomes_with_mnar.append(None) # MNAR
        elif inc == 'Medium' and np.random.rand() < 0.10:
            incomes_with_mnar.append(None)
        elif inc == 'Low' and np.random.rand() < 0.05:
            incomes_with_mnar.append(None)
        else:
            incomes_with_mnar.append(inc)

    df_customers = pd.DataFrame({
        'customer_id': customer_ids,
        'signup_date': [d.strftime('%Y-%m-%d') for d in cust_signups],
        'acquisition_channel': cust_channels,
        'customer_segment': cust_segments,
        'customer_city': cust_cities,
        'customer_state': cust_states,
        'latitude': cust_lats,
        'longitude': cust_lons,
        'ab_test_variant': ab_variants,
        'treatment_region': treatment_regions,
        'income_bracket': incomes_with_mnar
    })

    print("Generating Products & Categories...")
    categories_tree = [
        (1, 'All Products', None),
        (2, 'Electronics', 1),
        (3, 'Computers & Laptops', 2),
        (4, 'Audio & Accessories', 2),
        (5, 'Office & Furniture', 1),
        (6, 'Office Chairs & Desks', 5),
        (7, 'Stationery & Storage', 5),
        (8, 'Apparel & Fitness', 1),
        (9, 'Smart Wearables', 8),
        (10, 'Workout Gear', 8)
    ]
    df_cat_hierarchy = pd.DataFrame(categories_tree, columns=['category_id', 'category_name', 'parent_category_id'])

    subcat_map = {
        'Computers & Laptops': ('TECH-LAP', (400, 2200), (1200, 3200)),
        'Audio & Accessories': ('ELEC-AUD', (30, 350), (200, 1100)),
        'Office Chairs & Desks': ('FURN-OFF', (120, 850), (8000, 28000)),
        'Stationery & Storage': ('OFFC-STN', (15, 120), (300, 2500)),
        'Smart Wearables': ('WEAR-SMT', (80, 500), (100, 600)),
        'Workout Gear': ('FITN-APP', (25, 180), (400, 3000))
    }
    
    product_records = []
    prod_id = 1
    for cat_name, (prefix, price_range, weight_range) in subcat_map.items():
        items_in_cat = num_products // len(subcat_map)
        for j in range(1, items_in_cat + 1):
            p_id = f"PROD-{prod_id:04d}"
            sku = f"{prefix}-{prod_id:04d}"
            base_price = round(float(np.random.uniform(price_range[0], price_range[1])), 2)
            weight = int(np.random.uniform(weight_range[0], weight_range[1]))
            length = round(float(np.random.uniform(15, 60)), 1)
            width = round(float(np.random.uniform(10, 45)), 1)
            height = round(float(np.random.uniform(5, 30)), 1)
            cogs = round(base_price * np.random.uniform(0.52, 0.72), 2)
            product_records.append({
                'product_id': p_id,
                'product_category_name': cat_name,
                'product_sku': sku,
                'base_price': base_price,
                'cost_of_goods_sold': cogs,
                'product_weight_g': weight,
                'product_length_cm': length,
                'product_width_cm': width,
                'product_height_cm': height
            })
            prod_id += 1
            
    df_products = pd.DataFrame(product_records)

    print("Generating Orders and Items...")
    order_ids = [f"ORD-{i:06d}" for i in range(1, num_orders + 1)]
    
    # Assign orders to customers: some repeat buyers, some 1-off (follows Pareto/power law)
    cust_weights = np.random.pareto(a=1.5, size=num_customers)
    cust_weights /= cust_weights.sum()
    order_cust_indices = np.random.choice(num_customers, size=num_orders, p=cust_weights)
    order_cust_ids = [customer_ids[i] for i in order_cust_indices]
    
    # Generate realistic timestamps relative to customer signup
    order_dates = []
    policy_periods = []
    intervention_cutoff = datetime(2023, 10, 1)
    
    for c_idx in order_cust_indices:
        c_signup = cust_signups[c_idx]
        delta_days = int(np.random.exponential(scale=65))
        o_date = c_signup + timedelta(days=delta_days, hours=int(np.random.randint(0, 24)), minutes=int(np.random.randint(0, 60)))
        if o_date > datetime(2024, 6, 30):
            o_date = datetime(2024, 6, int(np.random.randint(1, 29)))
        order_dates.append(o_date)
        policy_periods.append('post_policy' if o_date >= intervention_cutoff else 'pre_policy')
        
    order_statuses = np.random.choice(['delivered', 'shipped', 'cancelled', 'returned'], size=num_orders, p=[0.88, 0.05, 0.04, 0.03])
    
    delivered_dates = []
    estimated_dates = []
    delivery_delays_days = []
    
    for i in range(num_orders):
        p_date = order_dates[i]
        status = order_statuses[i]
        est_days = int(np.random.randint(4, 9))
        est_date = p_date + timedelta(days=est_days)
        estimated_dates.append(est_date.strftime('%Y-%m-%d %H:%M:%S'))
        
        # MAR: delivery date is strictly missing if status is cancelled or currently shipped
        if status in ['cancelled', 'shipped']:
            delivered_dates.append(None)
            delivery_delays_days.append(np.nan)
        else:
            # actual delivery delay influenced by distance and state policy
            actual_days = int(np.random.normal(5.5, 2.0))
            actual_days = max(1, actual_days)
            deliv_date = p_date + timedelta(days=actual_days, hours=int(np.random.randint(1, 12)))
            delivered_dates.append(deliv_date.strftime('%Y-%m-%d %H:%M:%S'))
            delivery_delays_days.append(actual_days)

    payment_methods = np.random.choice(['credit_card', 'upi_instant', 'debit_card', 'voucher'], size=num_orders, p=[0.60, 0.22, 0.12, 0.06])
    installments = [1 if pm in ['upi_instant', 'voucher'] else int(np.random.choice([1, 2, 3, 6, 12], p=[0.55, 0.20, 0.12, 0.08, 0.05])) for pm in payment_methods]

    # Sample product and build order items
    prod_indices = np.random.choice(len(df_products), size=num_orders)
    item_prices = []
    item_cogs = []
    item_skus = []
    item_weights = []
    item_categories = []
    freight_values = []
    discounts = []
    
    for idx, o_idx in zip(prod_indices, range(num_orders)):
        p = df_products.iloc[idx]
        b_price = p['base_price']
        weight = p['product_weight_g']
        
        # Freight correlated with weight and customer distance
        freight = round(float(8.5 + (weight / 1000.0) * 1.8 + np.random.normal(0, 1.2)), 2)
        freight = max(5.0, freight)
        
        # Discounts: 65% no discount, 35% with 5% to 25% discount
        disc_pct = 0.0 if np.random.rand() > 0.35 else round(float(np.random.choice([0.05, 0.10, 0.15, 0.20, 0.25])), 2)
        discount_val = round(b_price * disc_pct, 2)
        
        item_prices.append(b_price)
        item_cogs.append(p['cost_of_goods_sold'])
        item_skus.append(p['product_sku'])
        item_weights.append(weight)
        item_categories.append(p['product_category_name'])
        freight_values.append(freight)
        discounts.append(discount_val)

    # Reviews and text
    review_ids = [f"REV-{i:06d}" for i in range(1, num_orders + 1)]
    review_scores = []
    review_comments = []
    
    positive_phrases = [
        "Outstanding quality! The SKU {sku} arrived ahead of schedule and works flawlessly.",
        "Very pleased with this purchase. Premium build and excellent packaging.",
        "High performance, very reliable item. Recommended to friends.",
        "Great value for money, prompt delivery and exactly as described in specs."
    ]
    negative_phrases = [
        "Extremely disappointing. The item arrived with damaged box and delayed delivery.",
        "Poor quality control. Failed after two days of usage. Seeking full refund.",
        "Terrible shipping delay. Order was stuck in transit for over a week.",
        "Does not match description. Low quality materials for SKU {sku}."
    ]
    neutral_phrases = [
        "Average product. Works as expected but nothing exceptional for the price.",
        "Decent shipping speed, package was intact. Standard quality.",
        "Packaging could be improved, but item functions reasonably well."
    ]

    for i in range(num_orders):
        status = order_statuses[i]
        delay = delivery_delays_days[i]
        sku = item_skus[i]
        
        # Review score correlation with delivery delay and cancellations
        if status == 'cancelled':
            score = 1
            comment = f"Order was cancelled without clear explanation. Very frustrated with service."
        elif np.isnan(delay) or delay > 8:
            score = int(np.random.choice([1, 2, 3], p=[0.55, 0.35, 0.10]))
            comment = np.random.choice(negative_phrases).format(sku=sku)
        elif delay <= 3:
            score = int(np.random.choice([4, 5], p=[0.25, 0.75]))
            comment = np.random.choice(positive_phrases).format(sku=sku)
        else:
            score = int(np.random.choice([2, 3, 4, 5], p=[0.10, 0.30, 0.40, 0.20]))
            comment = np.random.choice(neutral_phrases).format(sku=sku)
            
        review_scores.append(score)
        # MCAR: ~32% of customers leave a score but completely skip writing a text review
        if np.random.rand() < 0.32:
            review_comments.append(None) # MCAR
        else:
            review_comments.append(comment)

    # Assemble master DataFrame
    print("Assembling Master DataFrame...")
    cust_dict = df_customers.set_index('customer_id').to_dict('index')
    
    master_records = []
    for i in range(num_orders):
        cid = order_cust_ids[i]
        cinfo = cust_dict[cid]
        p_timestamp = order_dates[i]
        
        price = item_prices[i]
        disc = discounts[i]
        freight = freight_values[i]
        cogs = item_cogs[i]
        total_order_val = round((price - disc) + freight, 2)
        net_margin = round((price - disc) - cogs, 2)
        
        master_records.append({
            'order_id': order_ids[i],
            'customer_id': cid,
            'customer_state': cinfo['customer_state'],
            'customer_city': cinfo['customer_city'],
            'customer_segment': cinfo['customer_segment'],
            'acquisition_channel': cinfo['acquisition_channel'],
            'latitude': round(cinfo['latitude'], 4),
            'longitude': round(cinfo['longitude'], 4),
            'ab_test_variant': cinfo['ab_test_variant'],
            'treatment_region': cinfo['treatment_region'],
            'income_bracket': cinfo['income_bracket'],
            'order_status': order_statuses[i],
            'order_purchase_timestamp': p_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'order_delivered_timestamp': delivered_dates[i],
            'order_estimated_delivery_timestamp': estimated_dates[i],
            'policy_period': policy_periods[i],
            'payment_method': payment_methods[i],
            'payment_installments': installments[i],
            'product_id': df_products.iloc[prod_indices[i]]['product_id'],
            'product_category_name': item_categories[i],
            'product_sku': item_skus[i],
            'base_price': price,
            'discount_amount': disc,
            'freight_value': freight,
            'cost_of_goods_sold': cogs,
            'total_order_amount': total_order_val,
            'net_profit_margin': net_margin,
            'product_weight_g': item_weights[i],
            'delivery_days': delivery_delays_days[i],
            'review_id': review_ids[i],
            'review_score': review_scores[i],
            'review_comment_message': review_comments[i]
        })

    df_master = pd.DataFrame(master_records)
    
    # Save CSV and Parquet
    csv_path = os.path.join(output_dir, "enterprise_retail_analytics.csv")
    parquet_path = os.path.join(output_dir, "enterprise_retail_analytics.parquet")
    
    print(f"Saving Master CSV to {csv_path}...")
    df_master.to_csv(csv_path, index=False)
    
    print(f"Saving Master Parquet to {parquet_path}...")
    df_master.to_parquet(parquet_path, engine='pyarrow', index=False)

    # Web Funnel simulation
    print("Generating Web Funnel & Sessions...")
    steps_hierarchy = ['1_homepage', '2_search_browse', '3_product_detail', '4_add_to_cart', '5_checkout', '6_payment_complete']
    funnel_records = []
    
    for s_idx in range(1, num_sessions + 1):
        s_id = f"SESS-{s_idx:07d}"
        cid = np.random.choice(customer_ids)
        cinfo = cust_dict[cid]
        device = np.random.choice(['Mobile', 'Desktop', 'Tablet'], p=[0.60, 0.32, 0.08])
        variant = cinfo['ab_test_variant']
        
        # Treatment has slightly higher progression
        drop_probs = [0.82, 0.70, 0.55, 0.65, 0.78] if variant == 'treatment_new_ui' else [0.80, 0.65, 0.50, 0.60, 0.72]
        
        curr_step_idx = 0
        for p in drop_probs:
            if np.random.rand() < p:
                curr_step_idx += 1
            else:
                break
                
        reach_step = steps_hierarchy[curr_step_idx]
        is_converted = 1 if reach_step == '6_payment_complete' else 0
        s_date = datetime(2023, 1, 1) + timedelta(days=int(np.random.randint(0, 540)))
        
        funnel_records.append({
            'session_id': s_id,
            'customer_id': cid,
            'device_type': device,
            'ab_test_variant': variant,
            'furthest_funnel_step': reach_step,
            'converted': is_converted,
            'session_date': s_date.strftime('%Y-%m-%d')
        })
        
    df_funnel = pd.DataFrame(funnel_records)

    # Populate SQLite Database
    db_path = os.path.join(output_dir, "analytics_warehouse.db")
    print(f"Populating Relational SQLite DB at {db_path}...")
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    
    df_customers.to_sql('customers', conn, index=False)
    
    df_orders = df_master[['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 
                           'order_delivered_timestamp', 'order_estimated_delivery_timestamp', 
                           'policy_period', 'payment_method', 'payment_installments', 'total_order_amount']].copy()
    df_orders.to_sql('orders', conn, index=False)
    
    df_items = df_master[['order_id', 'product_id', 'product_sku', 'base_price', 'discount_amount', 
                          'freight_value', 'cost_of_goods_sold', 'net_profit_margin']].copy()
    df_items['order_item_id'] = 1
    df_items.to_sql('order_items', conn, index=False)
    
    df_products.to_sql('products', conn, index=False)
    df_cat_hierarchy.to_sql('categories_hierarchy', conn, index=False)
    
    df_revs = df_master[['review_id', 'order_id', 'review_score', 'review_comment_message']].copy()
    df_revs.to_sql('reviews', conn, index=False)
    
    df_funnel.to_sql('web_funnel', conn, index=False)
    
    conn.commit()
    conn.close()

    print(f"Data Generation Complete! All assets stored in {output_dir}")
    print(f"- Master CSV: {csv_path} ({os.path.getsize(csv_path)/(1024*1024):.2f} MB)")
    print(f"- Master Parquet: {parquet_path} ({os.path.getsize(parquet_path)/(1024*1024):.2f} MB)")
    print(f"- SQLite DB: {db_path} ({os.path.getsize(db_path)/(1024*1024):.2f} MB)")

if __name__ == '__main__':
    generate_all_data()
