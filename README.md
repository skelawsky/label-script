# label-script-from-kml-file
Data filtering script to make clean label for locations this case a customers locations.

## How to use
Just open .py file and in the console if asked type filetoread.kml path and filetosave.txt path


For example

##### INPUT
        <Placemark id="1.11.1">
				<name>Adana Kebab</name>
				<address>Multikino Ursynów, Aleja Komisji Edukacji Narodowej 60, 02-777 Warszawa</address>
				<phoneNumber>535 268 268</phoneNumber>
				<snippet>Multikino Ursynów, Aleja Komisji Edukacji Narodowej 60, 02-777 Warszawa</snippet>
				<description><![CDATA[<!DOCTYPE html><html><head></head><body><script type="text/javascript">window.location.href="https://www.google.com/earth/rpc/entity?lat=52.1824&lng=21.0266&fid=0x47193282429e8973:0xa49082e5fdb810d0&hl=pl&gl=pl&client=earth-client&cv=7.3.3.7786&useragent=GoogleEarth/7.3.3.7786(Windows;Microsoft Windows (6.2.9200.0);pl;kml:2.2;client:Pro;type:default)";</script></body></html>]]></description>
				<styleUrl>#listing_F</styleUrl>
				<ExtendedData>
					<Data name="placepageUri">
						<value>https://www.google.com/earth/rpc/entity?lat=52.1824&amp;lng=21.0266&amp;fid=0x47193282429e8973:0xa49082e5fdb810d0&amp;hl=pl&amp;gl=pl&amp;client=earth-client&amp;cv=7.3.3.7786&amp;useragent=GoogleEarth/7.3.3.7786(Windows;Microsoft Windows (6.2.9200.0);pl;kml:2.2;client:Pro;type:default)</value>
					</Data>
				</ExtendedData>
				<Point>
					<coordinates>21.0463889,52.14972219999999,0</coordinates>
				</Point>
			</Placemark>
			<Placemark id="1.9.1">
				<name>Adana Kebab</name>
				<address>Belgradzka 21A, 02-793 Warszawa</address>
				<phoneNumber>535 258 258</phoneNumber>
				<snippet>Belgradzka 21A, 02-793 Warszawa</snippet>
				<description><![CDATA[<!DOCTYPE html><html><head></head><body><script type="text/javascript">window.location.href="https://www.google.com/earth/rpc/entity?lat=52.1824&lng=21.0266&fid=0x47192d82e910f65b:0xdd4e653cab76acd9&hl=pl&gl=pl&client=earth-client&cv=7.3.3.7786&useragent=GoogleEarth/7.3.3.7786(Windows;Microsoft Windows (6.2.9200.0);pl;kml:2.2;client:Pro;type:default)";</script></body></html>]]></description>
				<styleUrl>#listing_F</styleUrl>
				<ExtendedData>
					<Data name="placepageUri">
						<value>https://www.google.com/earth/rpc/entity?lat=52.1824&amp;lng=21.0266&amp;fid=0x47192d82e910f65b:0xdd4e653cab76acd9&amp;hl=pl&amp;gl=pl&amp;client=earth-client&amp;cv=7.3.3.7786&amp;useragent=GoogleEarth/7.3.3.7786(Windows;Microsoft Windows (6.2.9200.0);pl;kml:2.2;client:Pro;type:default)</value>
					</Data>
				</ExtendedData>
				<Point>
					<coordinates>21.0548131,52.13876699999999,0</coordinates>
				</Point>
			</Placemark>
			
##### OUTPUT

>Adana KebabMultikino Ursynów, Aleja Komisji Edukacji Narodowej 60, 02-777 Warszawa535 268 268
>Adana KebabBelgradzka 21A, 02-793 Warszawa535 258 258
			
			