# Section 3: Using ELK Dashboards

### Purpose

Learn how to use ELK server to analyze Akamai Datastream data.

## Steps

1. DataLoading:
   - Open your LAMP website (which you created in section 1) to page: `<your_lamp_hostname>/ds2.html` and enter credentials to load data.
2. Discover Section:
   - What is the most common status code? Least common?
   - What reqPath has the largest ‘totalBytes’?
3. Dashboard Section:
   - Which country has the most http 403 response codes?
   - What files are larger than 300kB?
4. DevTools Section:
   - Get count of records datastream index with:GET datastream2/\_count
   - Load more data via DataLoader site and confirm count increases

## Visualize Section

Create an offload hits lens to show offload by resource.

1. Go to ‘Left Nav -> Visualize Library’
2. Click ‘Create Visualization -> Lens’
3. Switch visualization from ‘Bar vertical stacked’ to ‘Table’
4. In ‘Rows’ select field ‘reqPath’
5. In ‘Number of Values’ select ‘20’
6. Select ‘Close’ at bottom
7. In ‘Metrics’ click ‘+’ and then ‘Formula’ and add this formula to calculate offload: count(cacheStatus,kql='"cacheStatus":"1"')/count(cacheStatus)
8. Under appearance select ‘Value Format’ of ‘Percent’
9. Save with name of ‘Offload by Path’ and add to new dashboard and called ‘Akamai Offload’
10. Create another table for ‘Offload by Country’ and add it to the dashboard ‘Akamai Offload’
