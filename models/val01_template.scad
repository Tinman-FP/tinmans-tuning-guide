// VAL01: functional bracket and fit coupon, the last test before a filament
// profile is called TUNED. Tinmans Tuning Guide, chapter 09. CC BY 4.0.
// Change only `label` (material and revision, up to about 8 characters).
//
// Part 1: a bracket: base 70 x 40 x 8 with a cable channel underneath
//   (40 mm bridge under a 4 mm deck), upright wall 70 x 6, 38 tall overall, with a
//   40 x 12 window (40 mm lintel bridge), two 45-degree gussets, a 14 mm boss with a
//   5 mm bore standing on the bridge deck, two 5.5 mm (M5 clearance) and two 3.4 mm
//   (M3 clearance) holes, and the debossed label.
// Part 2: a fit coupon: four 8.0 mm holes and four pins at 7.9 / 7.8 / 7.7 / 7.6 mm
//   (0.1 / 0.2 / 0.3 / 0.4 mm diametral clearance), pins marked with 1-4 dimples on top.
label = "PCTG r7";
$fn = 128;

module gusset(x) {
  translate([x, 0, 0]) rotate([90, 0, 90]) linear_extrude(4)
    polygon([[14, 8], [34, 8], [34, 28]]);
}

module bracket() {
  difference() {
    union() {
      cube([70, 40, 8]);                          // base
      translate([0, 34, 0]) cube([70, 6, 38]);    // upright wall
      gusset(10); gusset(56);                     // 45-degree gussets
      translate([35, 17, 0]) cylinder(d = 14, h = 18);   // boss on the deck
    }
    translate([15, -1, -1]) cube([40, 36, 5]);    // cable channel: 40 wide, 4 tall, deck z 4..8
    translate([15, 33, 20]) cube([40, 8, 12]);    // window 40 x 12 in the wall, lintel z 32..38
    for (p = [[6, 6], [64, 6]]) translate([p[0], p[1], -1]) cylinder(d = 5.5, h = 10);   // M5 clearance
    for (p = [[5, 24], [65, 24]]) translate([p[0], p[1], -1]) cylinder(d = 3.4, h = 10); // M3 clearance
    translate([35, 17, -1]) cylinder(d = 5, h = 20);                                     // boss bore
    translate([35, 5, 7.4]) linear_extrude(1) text(label, size = 4.5, halign = "center", valign = "center");
  }
}

module fit_coupon() {
  difference() {
    cube([60, 14, 5]);
    for (i = [0:3]) translate([9 + i * 14, 7, -1]) cylinder(d = 8.0, h = 7);
  }
  for (i = [0:3]) translate([9 + i * 14, 26, 0]) difference() {
    cylinder(d = 7.9 - i * 0.1, h = 12);
    for (k = [0:i]) translate([-1.5 + k * 1.0, 0, 11.4]) cylinder(d = 0.8, h = 1, $fn = 24);  // 1-4 dimples
  }
}

bracket();
translate([0, -45, 0]) fit_coupon();
