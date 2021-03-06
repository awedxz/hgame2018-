import gmpy2

n = 0x6060e43632ae2bb9e3daa8a32b75df63806656562b6a9171def5bcda9ed084caa971adf8772d43f61bf4b785f1b8db55f242c59c6ffc4b66fd91108d8d9c4b854ecfbbfe80487de9f77c3b33af0158c7c1bc7a32c78e7f9573eec0f90e61184d260af75590bd86d8e8fcfece10dac3c6e1a4d82ea63ad81ad75aca0ebcadd8a7cdcfb90438523ad672040ac3737b4b42c77642b48b4a3da54191a365b091e62706c1738c8d97e3906eafb6770b257743c814f56b6904c5ec541964d1180cd9ffdc4bfa103a62119bd454d5d3d7aa39fe303af684176fa8d543d424bc983a0925a8711957335e62f9a01e34e3aa80a9222300b12aaa6771723a2a8c29b03d7dd9
g = 0x6060e43632ae2bb9e3daa8a32b75df63806656562b6a9171def5bcda9ed084caa971adf8772d43f61bf4b785f1b8db55f242c59c6ffc4b66fd91108d8d9c4b854ecfbbfe80487de9f77c3b33af0158c7c1bc7a32c78e7f9573eec0f90e61184d260af75590bd86d8e8fcfece10dac3c6e1a4d82ea63ad81ad75aca0ebcadd8a792dd3015bc74fe813112e1d87dfcb006d6226e00c75f707ff43a0ba50348566100ff437498a17c14677d7e8234cce154211aaea325119659ed587afa16ec3c9c9da242fadd996d52765a2c647c0a39a309815488673c9f6f36cd3bcceaa841c0d57338032e974705ba8371a17956602799a5d4b8008ffa865f3eb38d90d169e9
c = 0xb23aef818896a91c14ec2514cf4dd20ad4f737c356a1f7a7558a0756473db46acff90f7a83eee3cfe0c190cd73c3041e9351f109f6cc52f228e5c38e6dc160c511da466184e275e9f69a1c46adfe8df88e267b55d284fc3f099d2c6ab4628fc57690aacceaad106617534ab6b062c0452ff4c77637f049be13cb7c8b209c022a70e060713e43a5f0abe0e0cebc5ec8206239af25d5e5a67cb6a45d5cf131149adca33eb739428b957da8ad378284fbba0f535e807e179e04e4bec953eb83fad414d4ea7925f41189ee8d18b6a1a08bd25e5b30c1fa5d469e26a65f6a64f12a585c70d0c018a52fbe341ead92f61b1e0c1922c7b05b415250f351064570efbcb

sols = {(0, 0)}

for m in xrange(1111):
    print m, "bits", len(sols), "candidates"
    sols2 = set()
    mask = (2 << m) - 1
    for x, y in sols:
        if x * y == n:
            d = gmpy2.invert(65537, (x-1)*(y-1))
            print hex(pow(c, d, n))
            quit()
        for bx in xrange(2):
            for by in xrange(2):
                xx = x + (bx << m)
                yy = y + (by << m)

                if (xx * yy) & mask != n & mask:
                    continue
                gg = (xx * yy) - (xx ^ yy)
                if gg & mask != g & mask:
                    continue
                sols2.add((xx, yy))
    sols = sols2


# flag = "hgame{xxxxxxxxxxxxx}"