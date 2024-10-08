PGDMP                      |            audioplayer    14.5    16.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    24637    audioplayer    DATABASE     m   CREATE DATABASE audioplayer WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE audioplayer;
                postgres    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false                       0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    4            �            1259    24647    album    TABLE     �   CREATE TABLE public.album (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    release_date character varying
);
    DROP TABLE public.album;
       public         heap    postgres    false    4            �            1259    24646    album_id_seq    SEQUENCE     �   ALTER TABLE public.album ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.album_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    212    4            �            1259    24658    artist    TABLE     c   CREATE TABLE public.artist (
    id integer NOT NULL,
    stage_name character varying NOT NULL
);
    DROP TABLE public.artist;
       public         heap    postgres    false    4            �            1259    24657    artist_id_seq    SEQUENCE     �   ALTER TABLE public.artist ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.artist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215    4            �            1259    24639    song    TABLE     �   CREATE TABLE public.song (
    id integer NOT NULL,
    name character varying NOT NULL,
    hash_name character varying NOT NULL
);
    DROP TABLE public.song;
       public         heap    postgres    false    4            �            1259    24654 
   song_album    TABLE     y   CREATE TABLE public.song_album (
    id integer NOT NULL,
    song_id integer NOT NULL,
    album_id integer NOT NULL
);
    DROP TABLE public.song_album;
       public         heap    postgres    false    4            �            1259    24673    song_album_id_seq    SEQUENCE     �   ALTER TABLE public.song_album ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.song_album_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    213    4            �            1259    24663    song_artist    TABLE     b   CREATE TABLE public.song_artist (
    song_id integer NOT NULL,
    artist_id integer NOT NULL
);
    DROP TABLE public.song_artist;
       public         heap    postgres    false    4            �            1259    24638    song_id_seq    SEQUENCE     �   ALTER TABLE public.song ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.song_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    4    210                      0    24647    album 
   TABLE DATA           D   COPY public.album (id, name, description, release_date) FROM stdin;
    public          postgres    false    212   �                 0    24658    artist 
   TABLE DATA           0   COPY public.artist (id, stage_name) FROM stdin;
    public          postgres    false    215   �                 0    24639    song 
   TABLE DATA           3   COPY public.song (id, name, hash_name) FROM stdin;
    public          postgres    false    210   <                 0    24654 
   song_album 
   TABLE DATA           ;   COPY public.song_album (id, song_id, album_id) FROM stdin;
    public          postgres    false    213   Y       	          0    24663    song_artist 
   TABLE DATA           9   COPY public.song_artist (song_id, artist_id) FROM stdin;
    public          postgres    false    216   v                  0    0    album_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.album_id_seq', 52, true);
          public          postgres    false    211                       0    0    artist_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.artist_id_seq', 4, true);
          public          postgres    false    214                       0    0    song_album_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.song_album_id_seq', 147, true);
          public          postgres    false    217                       0    0    song_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.song_id_seq', 153, true);
          public          postgres    false    209            r           2606    24653    album album_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.album
    ADD CONSTRAINT album_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.album DROP CONSTRAINT album_pkey;
       public            postgres    false    212            v           2606    32830    artist artist_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.artist DROP CONSTRAINT artist_pkey;
       public            postgres    false    215            t           2606    24678    song_album song_album_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.song_album
    ADD CONSTRAINT song_album_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.song_album DROP CONSTRAINT song_album_pkey;
       public            postgres    false    213            p           2606    24645    song song_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY public.song
    ADD CONSTRAINT song_pkey PRIMARY KEY (id);
 8   ALTER TABLE ONLY public.song DROP CONSTRAINT song_pkey;
       public            postgres    false    210               ?   x�35�0���/6\�pa/M�b���
�_�z����i`�g`�gd`d����� �%^         9   x�. ��1	Горшок
2	Князь
3	Noname
4	1
\.


?<            x������ � �            x������ � �      	      x������ � �     